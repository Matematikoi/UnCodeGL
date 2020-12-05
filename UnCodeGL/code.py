import UnCodeGL.source
from UnCodeGL.data_structures.trie import Trie
class Code:
    """
    Core class for Coding and Decoding.
    It has integrated core metrics to it.

    To create a new Code you need to pass the rule
    for the code as a dictionary. 


    Attributes:
        arity:
            An integer representing the code arity
        code_alphabet:
            A set containing the code alphabet
        source_alphabet:
            A set containing the source alphabet
    """
    __code_trie = None
    __source_trie = None

    def __init__(self, code_dictionary):
        """"
        Initiates the class using a code dictionary
        """
        self.code = validate_dictionary(code_dictionary)
        self.code_alphabet, self.source_alphabet, coding_output = set(),set(), ''
        self.code_words = set()
        for key, value in self.code.items():
            self.source_alphabet.add(key)
            coding_output += value
            self.code_words.add(value)
        for simbol in coding_output:
            self.code_alphabet.add(simbol)
        self.arity = len(self.code_alphabet)
    
    def is_prefix(self):
        """
            Uses a Trie data structure to determine
            if the code is prefix

            Returns:
                A boolean True if the code is prefix, False
                otherwise
        """
        return self.get_code_trie().is_prefix()

    @staticmethod
    def kraft_inequality_metric(words_length=None, arity=None):
        """Calculates Kraft Inequality for given word lengths
        
            Measures Kraft Inequality Metric defined as 

            .. math::
                \sum_{i} r^{-l_i} 

            where r means arity, and l sub i the length of 
            the ith word
            
            Also returns if an instantaneous code can be made with said words

            Typical Usage:

            .. highlight:: python
            .. code-block:: python

                >>> metric, can_be_inst = kraft_inequality_metric(words_length=[4,4,3,6],arity=2)
                >>> print(metric, can_be_inst)
                0.265625 True
                
                
            Args:
                words_length:
                    An list with the length of the words
                arity:
                    Arity of the code

            Returns:
                metric , can_be_instantaneous.
                Kraft Inequality metric.
                A boolean refering to whether or not a code
                with this word lenghts and arity exists.
                This is dependant on the metric being less than 1
        """
        if arity == None:
            raise Exception('arity can\'t be null')
        if type(arity) != int :
            raise Exception('arity must be an int')
        if words_length == None:
            raise Exception('words_length can not be null')
        
        metric = 0.0
        epsilon = 0.00001
        for l in words_length:
            metric += float(arity)**float(-l)
        return metric, metric + epsilon < 1

    
    def get_code_trie(self):
        """
            Returns a Trie data structure 
            from the words in the code
        """
        if self.__code_trie == None:
            self.__code_trie = Trie(self.code_alphabet)
            for word in self.code_words:
                self.__code_trie.insert(word)
        return self.__code_trie
            
            
        


def validate_dictionary(code_dictionary):
    """
    Validates that a given dictionary is good to use as a code
    """
    if type(code_dictionary) != dict :
        raise Exception('code_dictionary must be of type dict')

    for key,value in code_dictionary.items():
        if type(key) != str :
            raise Exception('code_dictionary keys must be of type str')
        if type(value) != str : 
            raise Exception('code_dictionary keys must be of type str')
    return code_dictionary

        