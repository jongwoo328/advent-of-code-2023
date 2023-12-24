package day1

val digit_words = listOf(
    "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
)
val digit_length_3 = listOf("one", "two", "six")
val digit_length_4 = listOf("four", "five", "nine")
val digit_length_5 = listOf("three", "seven", "eight")

fun wordToDigit(word: String): Int {
    return digit_words.indexOf(word) + 1
}

fun getFirstDigit(input: String): Int {
    for ((index, char) in input.withIndex()) {
        if (char.isDigit()) {
            return Integer.parseInt(char.toString())
        }

        if (index + 3 < input.length) {
            val words3 = input.substring(index, index + 3)
            if (words3 in digit_length_3) {
                return wordToDigit(words3)
            }
        }

        if (index + 4 < input.length) {
            val words4 = input.substring(index, index + 4)
            if (words4 in digit_length_4) {
                return wordToDigit(words4)
            }
        }

        if (index + 5 < input.length) {
            val words5 = input.substring(index, index + 5)
            if (words5 in digit_length_5) {
                return wordToDigit(words5)
            }
        }
    }
    throw Exception("No digit found")
}

fun getLastDigit(input: String): Int {
    for ((index, char) in input.reversed().withIndex()) {
        if (char.isDigit()) {
            return Integer.parseInt(char.toString())
        }

        if (input.length - index - 3 >= 0) {
            val words3 = input.substring(input.length - index - 3, input.length - index)
            if (words3 in digit_length_3) {
                return wordToDigit(words3)
            }
        }

        if (input.length - index - 4 >= 0) {
            val words4 = input.substring(input.length - index - 4, input.length - index)
            if (words4 in digit_length_4) {
                return wordToDigit(words4)
            }
        }

        if (input.length - index - 5 >= 0) {
            val words5 = input.substring(input.length - index - 5, input.length - index)
            if (words5 in digit_length_5) {
                return wordToDigit(words5)
            }
        }
    }
    throw Exception("No digit found")
}

fun getCalibrationValue2(input: String): Int {
    return getFirstDigit(input) * 10 + getLastDigit(input)
}

fun main() {
    val inputs = readFile()
    println(inputs.sumOf { getCalibrationValue2(it) })
}
