from typing import List


class binary_memory_sorter:

    def __init__(self):
        self.bynary_memory = []

    def binary_memory_manager(self, input_number_to_convert: int) -> None:
        output_bin_number = [int(x) for x in bin(input_number_to_convert)[2:].zfill(16)]
        self.bynary_memory.append(output_bin_number)

    def binary_memory_converter(self, number_word_lens: List[bool]) -> int:
        dec_number = 0
        for iterator in range(len(number_word_lens)):
            dec_number += number_word_lens[iterator] * (2 ** (len(number_word_lens) - iterator - 1))
        return dec_number


    def reverse_binary_sort(self) -> None:

        for iterator in range(len(self.bynary_memory)):

            for j_iterator in range(len(self.bynary_memory) - iterator - 1):

                if self.bynary_memory[j_iterator] < self.bynary_memory[j_iterator + 1]:

                    self.bynary_memory[j_iterator], self.bynary_memory[j_iterator + 1] \
                        = self.bynary_memory[j_iterator + 1], self.bynary_memory[j_iterator]

    def bubble_sort_binary_memory(self) -> None:

        for iterator in range(len(self.bynary_memory)):

            for j_iterator in range(len(self.bynary_memory) - iterator - 1):

                if self.bynary_memory[j_iterator] > self.bynary_memory[j_iterator + 1]:
                    self.bynary_memory[j_iterator], self.bynary_memory[j_iterator + 1] \
                        = self.bynary_memory[j_iterator + 1], self.bynary_memory[j_iterator]



    def binary_conversion(self, number_to_convert: int) -> List[bool]:
        input_binary_number = [int(x) for x in bin(number_to_convert)[2:].zfill(16)]
        return input_binary_number



    def fetch_binary_matrix(self) -> List[List[bool]]:
        return self.bynary_memory

    def __str__(self) -> str:
        fetched_binary_matrix = self.fetch_binary_matrix()
        result_output = ""
        for iterator in range(len(fetched_binary_matrix)):
            for j_iterator in range(len(fetched_binary_matrix[iterator]) - 1):
                result_output += str(fetched_binary_matrix[iterator][j_iterator]) + ","
            result_output += str(fetched_binary_matrix[iterator][len(fetched_binary_matrix[iterator]) - 1]) + "\n"
        return result_output

    def retrieve_elements_in_range(self, lower_limit_to_move: int, upper_limit_to_move: int) -> List[List[bool]]:

        selected_words = []

        lower_limit_binary_word = self.binary_conversion(lower_limit_to_move)
        upper_binary_representation = self.binary_conversion(upper_limit_to_move)
        for i in range(len(self.bynary_memory)):
            if lower_limit_binary_word < self.bynary_memory[i] < upper_binary_representation:
                selected_words.append(self.bynary_memory[i])
        return selected_words


def between_print_result():

    retrieved_elements = binary_sorter.retrieve_elements_in_range(lower_limit_binary_word_1,
                                                                  upper_binary_representation_1)
    for sublist in retrieved_elements:

        print(",".join(str(element) for element in sublist))


if __name__ == "__main__":

    binary_sorter = binary_memory_sorter()
    num_collection = [123, 556, 1231, 871, 23, 155, 887, 2232, 7754, 34]
   
    for move_num in num_collection:
        binary_sorter.binary_memory_manager(move_num)

    lower_limit_binary_word_1 = 500
    upper_binary_representation_1 = 50000

    print("Binary Memory Contents:\n" + (str(binary_sorter)))
    print("Words placed in between:\n", binary_sorter.binary_conversion(lower_limit_binary_word_1),
          "\n\t\t\t\t\t\tand\n", binary_sorter.binary_conversion(upper_binary_representation_1), "\n")

    between_print_result()
    binary_sorter.bubble_sort_binary_memory()

    print("\nThe output is arranged in descending order:\n" + (str(binary_sorter)))
    binary_sorter.reverse_binary_sort()
    print("The elements have been sorted in ascending order:\n" + (str(binary_sorter)))