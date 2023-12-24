package day1

import java.io.File

fun readFile(): List<String> {
    val fileName = "day1-1.input"
    val file = File("./kotlin/src/main/kotlin/day1/$fileName")
    val lines = file.readLines()
    return lines
}

fun getCalibrationValue(input: String): Int {
    val calibrationValueList = mutableListOf<Int>()

    for (char in input) {
        if (char.isDigit()) {
            calibrationValueList.add(Integer.parseInt(char.toString()))
            break
        }
    }

    for (char in input.reversed()) {
        if (char.isDigit()) {
            calibrationValueList.add(Integer.parseInt(char.toString()))
            break
        }
    }

    return calibrationValueList.joinToString("").toInt()
}

fun main() {
    val inputs = readFile()

    println(inputs.sumOf { getCalibrationValue(it) })
}


