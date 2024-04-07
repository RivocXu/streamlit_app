# Week 9 Mini Project
> Puyang(Rivoc) Xu (px16)

This project is a simple Rust Command-Line Tool with Testing. The main function is read the data of characters from a .csv file. Then we can use Rust Command-Line Tool to run this project. Unit tests are also included.

Testing report: [Report →](https://gitlab.com/RivocX/mini-project-8/-/blob/master/test_report.md?ref_type=heads)






## Preparation

pip3 install streamlit
pip3 freeze > requirements.txt
pip3 install streamlit transformers

pip3 install torch torchvision torchaudio
pip3 install tensorflow





The installation of `Cargo` is needed in this project.
Create a new cargo project:
```
cargo new cl_tool
```

Modify dependencies in `Cargo.toml`:
```
[dependencies]
csv = "1.1"
serde = { version = "1.0", features = ["derive"] }
clap = "2.33.3"
```

Write a lotr_characters.csv file.
![](./media/csv.png)

## Functions

### Features
- **Command-Line Interface**: Leveraging `clap`, the tool provides a user-friendly command-line interface for specifying the CSV file path and applying filters based on character name and/or race.
- **CSV Parsing**: Utilizes the `csv` crate to read and deserialize data from a specified CSV file into a vector of `Character` structs.
- **Flexible Filtering**: Allows filtering the character data based on provided name and/or race parameters. If no filters are applied, the tool outputs all characters from the CSV file.
- **Custom Data Structure**: Defines a `Character` struct to hold and represent character data, including fields for name, title, race, birthday, gender, weapon, and domain.

### Main Components
1. **Argument Parsing**: Parses command-line arguments for the CSV file path and optional filters for name and race.
2. **CSV Processing**: Reads the CSV file and deserializes its content into a vector of `Character` structs.
3. **Data Filtering**: Applies the optional name and race filters to the vector of characters, returning only those that match the criteria.
4. **Output**: Prints detailed information about each character that matches the filtering criteria to the standard output.

### Usage

The tool is invoked from the command line, with the CSV file path as a required argument and options for filtering by name (`-n` or `--name`) and race (`-r` or `--race`). The filtered character information is then printed to the standard output.


Build this project first:
```
cargo build --release
```
Then you can run with command line as following format:
```
./target/release/cl_tool <file> [OPTIONS]
```
For instance:
```
./target/release/cl_tool lotr_characters.csv --name "Frodo" --race "Hobbit"
./target/release/cl_tool lotr_characters.csv --race "Elf"
```

Run with cargo is also fine:
```
cargo build
```
```
cargo run -- lotr_characters.csv --name "Frodo" --race "Hobbit"
cargo run -- lotr_characters.csv --race "Hobbit"
```

## Testing report
The unit tests for this project ensure that the application's filtering logic accurately handles character data based on name and race criteria. By simulating a predefined set of "Lord of the Rings" characters, these tests verify the application's ability to apply filters individually or in combination, as well as its ability to return all characters when no filters are applied. Through these tests, we confirm the reliability and accuracy of the tool's core functionality, ensuring it operates as expected under a variety of conditions.

Detailed testing report: [Report →](https://gitlab.com/RivocX/mini-project-8/-/blob/master/test_report.md?ref_type=heads)


## Results & Screenshots

### Rust Command-Line Tools
![](./media/cl.png)

### Unit tests
![](./media/test.png)
