import numpy


class DoseFile(object):
    def __init__(self, file_name):
        self._load_egsphant(file_name)

    def _load_egsphant(self, file_name):
        data = open(file_name, "r", encoding="utf-8").read().split('\n')

        cur_line = 0

        m = int(data[cur_line].split().pop())
        cur_line += 1

        materials = {}
        for i in range(0, m):
            materials[i+1] = data[cur_line].split().pop()
            cur_line += 1
        self.materials = materials

        cur_line += 1

        x, y, z = list(map(int, data[cur_line].split()))
        self.shape = (z, y, x)
#         self.shape = (x,y,z)
        print((len(self.materials),) + self.shape)
        print(self.materials)

        self.size = numpy.multiply.reduce(self.shape)

        cur_line += 1

        positions = []
        for i in range(0,3):
            bounds = []
            while len(bounds) < [x, y, z][i]:
                line_positions = list(map(float, data[cur_line].split()))
                bounds += line_positions
                cur_line += 1
            positions.append(bounds)

        # recall that dimensions are read in order x, y, z
        positions = [positions[2], positions[1], positions[0]]

        self.positions = positions
        self.spacing = [numpy.diff(p) for p in self.positions]
        self.resolution = [s[0] for s in self.spacing if s.all()]
        self.origin = numpy.add( [p[0] for p in positions], numpy.array(self.resolution)/2.)

        assert len(self.resolution) == 3, "Non-linear resolution in either x, y or z."

        voxelsmaterial = []
        for k in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                for i in range(0, self.shape[2]):
                    voxelsmaterial += int(data[cur_line][i])
                cur_line += 1
            cur_line += 1

        self.voxelsmaterial = numpy.array(voxelsmaterial)
        assert len(self.voxelsmaterial) == self.size, "len of voxelsmaterial = {} (expect {})".format(len(self.voxelsmaterial), self.size)
        
        self.voxelsmaterial = self.voxelsmaterial.reshape((self.shape))
        assert self.voxelsmaterial.size == self.size, "Voxels material array size does not match that specified."

        voxelsdensity = []
        for k in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                line_data = list(map(float, data[cur_line].split()))
                voxelsdensity += line_data
                cur_line += 1
            cur_line += 1

        self.voxelsdensity = numpy.array(voxelsdensity)
        assert len(self.voxelsdensity) == self.size, "len of voxelsdensity = {} (expect {})".format(len(self.voxelsdensity), self.size)
        
        self.voxelsdensity = self.voxelsdensity.reshape((self.shape))
        assert self.voxelsdensity.size == self.size, "Voxels density array size does not match that specified."

        
    def dump(self, file_name):
        numpy.savez(file_name, materials=self.materials, voxelmaterial=self.voxelmaterial, voxeldensity=self.voxeldensity,
            x_positions=self.positions[0], y_positions=self.positions[1],
            z_positions=self.positions[2])

    def maxdensity(self):
        return self.voxelsdensity.max()
        
    def mindensity(self):
        return self.voxelsdensity.min()

    @property
    def x_extent(self):
        return self.positions[0][0], self.positions[0][-1]

    @property
    def y_extent(self):
        return self.positions[1][0], self.positions[1][-1]
    
    @property
    def z_extent(self):
        return self.positions[2][0], self.positions[2][-1]
