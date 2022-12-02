namespace CSharp.Day1;

public class Puzzle2
{
    public static void Main()
    {
        string text =
            File.ReadAllText(
                "/Users/tejuo/Library/CloudStorage/OneDrive-Personal/Programming/Advent of code/CSharp/Day1/input.txt");

        int answer = text.Split("\n\n")
            .Select(elf => elf.Split("\n")
                .Select(int.Parse)
                .Sum())
            .OrderDescending()
            .Take(3)
            .Sum();

        Console.WriteLine(answer);
    }
}