# write a class to compute the derivative of each single term
class single_term_derivative:
    def __init__(self,one_term_polynomial):  # intialize the term of the polynomial
        self._polynomial=str(one_term_polynomial)
    
    def calculate_derivative(self):
        exponential_index=self._polynomial.find("^")  # locate the "^" sign of each term of the polynomial
        if exponential_index == -1:  # can't find the "^" sign
            if self._polynomial[-1].isdigit():  # the term is constant
                return "0"
            elif len(self._polynomial) == 1 and self._polynomial[-1].isdigit() == False:  # the term is "x", for example
                return "1"
            elif len(self._polynomial) == 2 and self._polynomial[-1].isdigit() == False and self._polynomial.startswith("-"):  # the term is "-x", for example
                return "-1"
            elif len(self._polynomial) == 2 and self._polynomial[-1].isdigit() == False and self._polynomial.startswith("+"):
                return "1"
            else:
                if self._polynomial.startswith("+"):
                    return self._polynomial[1:-2]
                else:
                    return self._polynomial[:-2]  # the power is 1, return the coefficient as the derivative
        
        chosen_variable=self._polynomial[exponential_index-1]  # save the chosen variable 
        power=int(self._polynomial[exponential_index+1:])  # get the power of the term

        if self._polynomial.index(self._polynomial[exponential_index-1]) == 0:  # the term is x^2, for example
            coefficient=power
        elif self._polynomial.startswith("+") and self._polynomial.index(self._polynomial[exponential_index-1]) == 1:
            coefficient=power
        elif self._polynomial[:exponential_index-1] == "-":  # the term is -x^2, for example
            coefficient=-power
        else:
            coefficient=int(self._polynomial[:exponential_index-2])  # calculate the new coefficient 
            coefficient*=power
        
        power-=1

        # return the result in appropriate form
        if power == 1:
            return str(coefficient)+"*"+chosen_variable.lower()
        if coefficient == 1:
            return chosen_variable.lower()+"^"+str(power)
        if coefficient == -1:
            return "-"+chosen_variable.lower()+"^"+str(power)
        
        return str(coefficient)+"*"+chosen_variable.lower()+"^"+str(power)

def get_sign_index(polynomial):  # use the function to slice the whole polynomial to single terms
    plus_sign=[]
    minus_sign=[]
    for i in polynomial:
        if i == "+":
            plus_sign.append(polynomial.index(i))  # save the location of the "+" sign
            polynomial=polynomial.replace("+","0",1)  # avoid saving the first "+" repeatedly
        elif i == "-":
            minus_sign.append(polynomial.index(i))  # save the location of the "-" sign
            polynomial=polynomial.replace("-","0",1)  # avoid saving the first "-" repeatedly
    signs_index=plus_sign+minus_sign
    signs_index.sort()  # sort the sign index in ascending order
    return signs_index

def split_polynomial(polynomial,signs_index):  # save all the single terms of the polynomial into one list
    polynomial_split=[]
    if len(signs_index) == 1:  # the polynomial only has two terms
        polynomial_split.append(polynomial[:signs_index[0]])  # get the term before the sign
        polynomial_split.append(polynomial[signs_index[-1]:])  # get the term after the sign
    elif len(signs_index) != 1 and polynomial[0] == "-":
        for i in range(1,len(signs_index)):
            polynomial_split.append(polynomial[signs_index[i-1]:signs_index[i]])
        polynomial_split.append(polynomial[signs_index[-1]:])
    else:  # the polynomial has more than two terms
        polynomial_split.append(polynomial[:signs_index[0]])  # get the term before the first +/- sign
        for i in range(1,len(signs_index)):
            polynomial_split.append(polynomial[signs_index[i-1]+1:signs_index[i]])  # get the terms between the first and last sign
        polynomial_split.append(polynomial[signs_index[-1]:])  # get the term after the last +/- sign
    return polynomial_split

def single_term_derivative_list(polynomial_split):  # save derivative of all the terms into one list
    single_term_derivative_list=[]
    for i in polynomial_split:
        single_derivative=single_term_derivative(i).calculate_derivative()
        single_term_derivative_list.append(single_derivative)
    while "0" in single_term_derivative_list:
        single_term_derivative_list.remove("0")  # remove "0" terms
    return single_term_derivative_list

def final_derivative_expression(single_term_derivative_list):
    result=""
    for term in single_term_derivative_list:
        if str(term).startswith("-"):
            result+=str(term)
        else:
            result=result+"+"+str(term)  # if the result starts with "+", eliminate it
    if result.startswith("+"):
        result = result[1:]
    return result

def main():
    polynomial=str(input("Please input a polynomial in standard algebraic notation:"))

    a=get_sign_index(polynomial)
    b=split_polynomial(polynomial,a)
    c=single_term_derivative_list(b)
    d=final_derivative_expression(c)

    print("The first derivative of the polynomial is",d)
main()