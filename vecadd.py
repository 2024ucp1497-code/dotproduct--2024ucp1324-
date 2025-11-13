from multiprocessing import Pool

v1 = list(map(int, input("enter first vector:").split()))
v2 = list(map(int, input("enter second vector:").split()))

if len(v1) != len(v2):
                 print("Error")
                 
else :

      
      print("dot product result= ",sum(x*y for x,y in zip(v1,v2))) 

      with Pool() as pool:
      	result = pool.map(multiply,zip(v1,v2))
      print("parallelism dot product= ",p)

   	
  #hi bro 	

