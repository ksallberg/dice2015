import Control.Monad
import Data.List

type Pokemon = String
type Chain   = [Pokemon]
type Branch  = (Bool, Chain)

{-
λ> findLongest
    ["machamp","pinsir","rufflet","trapinch","heatmor","relicanth","haxorus",
     "starly","yamask","kricketune","exeggcute","emboar","registeel","loudred",
     "darmanitan","nosepp","petilil","landorus","seaking","girafarig","gabite",
     "emolga","audino"]
-}
pokemons :: [Pokemon]
pokemons =
    ["audino","bagon","baltoy","banette","bidoof","braviary","bronzor",
     "carracosta","charmeleon","cresselia","croagunk","darmanitan","deino",
     "emboar","emolga","exeggcute","gabite","girafarig","gulpin","haxorus",
     "heatmor","heatran","ivysaur","jellicent","jumpluff","kangaskhan",
     "kricketune","landorus","ledyba","loudred","lumineon","lunatone",
     "machamp","magnezone","mamoswine","nosepp","petilil","pidgeotto",
     "pikachu","pinsir","poliwrath","poochyena","porygon2","porygonz",
     "registeel","relicanth","remoraid","rufflet","sableye","scolipede",
     "scrafty","seaking","sealeo","silcoon","simisear","snivy","snorlax",
     "spoink","starly","tirtouga","trapinch","treecko","tyrogue","vigoroth",
     "vulpix","wailord","wartortle","whismur","wingull","yamask"]

increaseBranches :: [Branch] -> [Branch]
increaseBranches ls =
    let unex = keepNonExhausted ls
        ex   = [b | b@(exhausted, chain) <- ls, exhausted]
    in ex ++ concat [(increaseBranch un) | un <- unex]

increaseBranch :: Branch -> [Branch]
increaseBranch (True,  chain) = [(True, chain)]
increaseBranch (False, chain) = [(isExhausted nb, nb) |
                                 nb <- matchOneStep chain]

keepNonExhausted :: [Branch] -> [Branch]
keepNonExhausted ls = [b | b@(exhausted, chain) <- ls, not exhausted]

isExhausted :: Chain -> Bool
isExhausted ch = null $ matchOneStep ch

allExhausted :: [Branch] -> Bool
allExhausted br = and [exhausted | (exhausted, _) <- br]

-- Look at the last pokemon in a list, and match it with the first pokemon
-- in the list of all pokemons, the resulting list is strict (no duplicates)
matchOneStep :: Chain -> [Chain]
matchOneStep poke = (nub [nub $ poke ++ [toTest] | toTest <- pokemons,
                         lookFor == head toTest]) \\ [poke]
    where lookFor = (last . last) poke


-- In a chain of pokemons, add as many pokemons as possible
runMatching :: [Branch] -> [Branch]
runMatching brs =
    case allExhausted brs of
        True  -> brs
        False -> runMatching $ increaseBranches brs

test :: [Branch]
test = runMatching [(False, ["yamask"])]

findL :: Pokemon -> Chain
findL poke = foldr (\(_, this) longest ->
              case (length this) > (length longest) of
                  True  -> this
                  False -> longest)
        [] (runMatching [(isExhausted [poke], [poke])])

findAll :: [Chain]
findAll = map findL startLs
    where startLs = [poke | poke <- pokemons, not $ isExhausted [poke]]

findLongest :: Chain
findLongest = foldr (\ls longest ->
                    case (length ls) > (length longest) of
                        True  -> ls
                        False -> longest
                    ) [] findAll
