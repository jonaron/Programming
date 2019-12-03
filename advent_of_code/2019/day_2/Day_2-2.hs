main = do
    contents <- readFile "input.txt" 
    print $ discover 19690720 0 0 (read contents ::[Int])

discover :: Int -> Int -> Int -> [Int] -> Int
discover value noun verb (i:j:k:program)
    | head (run (i:noun:verb:program) 0) == value = (100*noun) + verb
    | verb == noun = discover value 0 (verb+1) (i:j:k:program)
    | otherwise = discover value (noun+1) verb (i:j:k:program)




run :: [Int] -> Int -> [Int]
run program pointer
    | program !! pointer == 1    = run (add program pointer) (pointer + 4)
    | program !! pointer == 2    = run (mult program pointer) (pointer + 4)
    | program !! pointer == 99   = program

add :: [Int] -> Int -> [Int]
add program pointer =
    replaceNth z ((program !! x) + (program !! y)) program
    where (x,y,z) = grabThree (pointer+1) program

mult :: [Int] -> Int -> [Int]
mult program pointer = 
    replaceNth z ((program !! x) * (program !! y)) program
    where (x,y,z) = grabThree (pointer+1) program

grabThree :: Int -> [a] -> (a,a,a)
grabThree n (x:y:z:xs) 
    | n == 0 = (x,y,z)
    | n > 2 = grabThree (n-3) xs
    | otherwise = grabThree (n-1) (y:z:xs)

replaceNth :: Int -> a -> [a] -> [a]
replaceNth _ _ [] = []
replaceNth n newVal (x:xs)
    | n == 0 = newVal:xs
    | otherwise = x:replaceNth (n-1) newVal xs