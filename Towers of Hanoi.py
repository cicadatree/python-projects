
# recursive function to solve Tower of Hanoi, where source, destination and auxiliary refer to the three towers in the game
def TowerOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source", source,"to destination",destination)
    TowerOfHanoi(n-1,auxiliary,destination,source)

n = 4

# A, B, C refer to the three rods in the game
TowerOfHanoi(n,'A','B','C')
