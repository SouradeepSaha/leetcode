class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        posX, posY = 0, 0
        
        for instr in instructions:
            if instr == "L":
                dirX, dirY = -dirY, dirX
            elif instr == "R":
                dirX, dirY = dirY, -dirX
            else:
                posX += dirX
                posY += dirY
        
        return (posX, posY) == (0, 0) or (dirX, dirY) != (0, 1)
