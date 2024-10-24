#
# Distributed under the OSI-approved Apache License, Version 2.0.  See
# accompanying file Copyright.txt for details.
#
# bpWriter_nonmpi.py : only works with non MPI version
#  Created on: Feb 2, 2017
#      Author: William F Godoy godoywf@ornl.gov

import numpy
import adios2

# User data
myArray = numpy.array([0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
Nx = myArray.size

#  adios
adios = adios2.ADIOS()

# ADIOS IO
bpIO = adios.DeclareIO("BPFile_N2N")

# ADIOS Variable name, shape, start, offset, constant dims
ioArray = bpIO.DefineVariable("bpArray", myArray, [], [], [Nx], adios2.ConstantDims)

# ADIOS Engine
bpFileWriter = bpIO.Open("npArray.bp", adios2.Mode.Write)
bpFileWriter.BeginStep()
bpFileWriter.Put(ioArray, myArray, adios2.Mode.Sync)
bpFileWriter.EndStep()
bpFileWriter.Close()
