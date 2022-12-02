package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

public class puzzle1 {
	public static void main(String[] args) {
		String text;
		try {
			text = Files.readString(Path.of("src/main/java/day1/input.txt"));
		} catch (IOException e) {
			throw new RuntimeException(e);
		}

		int answer = Arrays.stream(text.split("\n\n"))
				.mapToInt(elf -> Arrays.stream(elf.split("\n"))
						.mapToInt(Integer::parseInt).sum())
				.max()
				.orElseThrow();

		System.out.println(answer);
	}
}
