main = do
    contents <- readFile "input.txt" 
    print $ sum $ map (\x -> fuelreq $ read x ::Int) $ lines contents

fuelreq x = (div x 3) - 2