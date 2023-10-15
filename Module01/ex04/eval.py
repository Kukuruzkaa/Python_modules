class Evaluator:
    
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list) or len(coefs) != len(words):
            return -1
        sum = 0
        tuple_pair = zip(coefs, words)
        for pair in tuple_pair:
            if not isinstance(pair[0], float) and not isinstance(pair[1], str):
                return -1
            sum += pair[0] * len(pair[1])
        return sum
         
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list) or len(coefs) != len(words):
            return -1
        tuple_pair = zip(coefs, words)
        for pair in tuple_pair:
            if not isinstance(pair[0], float) and not isinstance(pair[1], str):
                return -1
        sum = 0
        for i, j in enumerate(words):
            sum += coefs[i] * len(j)
        return sum


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    # 32.0
    
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    # -1 
    
    words = ["Le", "Lorem"]
    coefs = [1.0, 2.0]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    # 12 
    
    words = ["Le"]
    coefs = [1.0]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    # 2 