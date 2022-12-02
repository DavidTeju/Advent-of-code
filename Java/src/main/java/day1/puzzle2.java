package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;

public class puzzle2 {
	public static void main(String[] args) {
		String text;
		try {
			text = Files.readString(Path.of("src/main/java/day1/input.txt"));
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
		
		int answer =
				Arrays.stream(text.split("\n\n"))
						.map(elf -> Arrays.stream(elf.split("\n"))
								.mapToInt(Integer::parseInt).sum())
						.sorted(Collections.reverseOrder())
						.limit(3)
						.reduce(Integer::sum)
						.orElseThrow();
		
		System.out.println(answer);
	}
}
