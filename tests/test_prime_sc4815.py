from prime_sc4815 import prime_sc4815

def test_is_prime():

        assert prime_sc4815.is_prime(2) == True
        assert prime_sc4815.is_prime(7) == True
        assert prime_sc4815.is_prime(8) == False
        assert prime_sc4815.is_prime(9) == False