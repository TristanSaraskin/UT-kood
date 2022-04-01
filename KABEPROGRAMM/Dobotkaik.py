#Magician
import math

X = [78, 103.286, 128.572, 153.858, 179.144, 204.43, 229.716, 255]
Y = [-50, -32.571, -15.142, 2.287, 19.716, 37.145, 54.574, 72]

x1 = X[]
y1 = Y[]
x2 = X[]
y2 = Y[]

dType.SetHOMECmdEx(api, 0, 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 4, 0,  45,  45, current_pose[7], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, x1,  y1,  0, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, x1,  y1,  (-40), current_pose[3], 1)
dType.SetEndEffectorSuctionCupEx(api, 1, 1)
dType.dSleep(1000)
dType.SetEndEffectorGripperEx(api, 1, 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, x1,  y1,  0, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, x2,  y2,  0, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, x2,  y2,  (-40), current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 0)
dType.dSleep(1000)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, x2,  y2,  0, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 4, (-90),  45,  45, current_pose[7], 1)
