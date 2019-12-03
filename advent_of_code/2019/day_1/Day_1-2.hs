main = do
    contents <- readFile "input.txt" 
    print $ sum $ map (\x -> fuelreq $ read x ::Int) $ lines contents

fuelreq x = (fuelreq' x) - x

fuelreq' x
    |x < 9      = x
    |otherwise  = (+) x $ fuelreq' $ nextfuel x

nextfuel x = (div x 3) - 2