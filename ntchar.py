from networktables import NetworkTables
import sys

print( "The arguments are: " , str(sys.argv))
# As a client to connect to a robot
NetworkTables.initialize(server='roborio-XXX-frc.local')
#sd = NetworkTables.getTable('SmartDashboard')

#sd.putNumber('someNumber', 1234)
#otherNumber = sd.getNumber('otherNumber')