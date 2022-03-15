
## Files
- .gitignore        : ignores any temporary files
- code/land.py      : console prints summary statistics for the meteorite landings, given a json datafile.
- code/test_land.py	: tests the code/land.py file via pytest.
- data/data.json    : example meteorite landing data
- Dockerfile        : a docker instruction set to help build a docker container for the program
- Makefile          : a makefile to automate the clean / build / run / push commands for the docker container



<details open>
<summary>data.json (HEAD)</summary>

```
{
 "meteorite_landings": [
   {
     "name": "Ruiz",
     "id": "10001",
     "recclass": "L5",
     "mass (g)": "21",
     "reclat": "50.775",
     "reclong": "6.08333",
     "GeoLocation": "(50.775, 6.08333)"
   },
   {
     "name": "Beeler",
     "id": "10002",
     "recclass": "H6",
     "mass (g)": "720",
     "reclat": "56.18333",
     "reclong": "10.23333",
     "GeoLocation": "(56.18333, 10.23333)"
   },
  ]
}
```

</details>

## Installation & Usage

### Docker Container

<details>
<summary>Details</summary>

#### Install
- Note `docker run` will also pull the necessary image, but if you need to pull the image:
  - `docker pull akhilsadam/ml_data_analysis:hw04`
- Install Docker:
  - `apt-get install docker` (if you are on an Ubuntu machine)
#### Run 
- Test
  - `docker run -it --rm akhilsadam/ml_data_analysis:hw04 pytest code`
- Run 
  - Replace `<pathtodatafile.json>` with a path to your datafile.
  - `docker run --rm -v ${PWD}:/data akhilsadam/ml_data_analysis:hw04 land.py data/<pathtodatafile.json>`
  - To see example output:
  - `docker run --rm akhilsadam/ml_data_analysis:hw04 land.py data/data.json`

</details>

### From Source

<details>
<summary>Details</summary>

- Please note that source builds only support Python3 on Ubuntu 20.04, and are written in that fashion. Your mileage may vary for other systems.
#### Install
- First, install all dependencies:
```
apt-get install zlib1g python3 python3-pip -y
pip3 install numpy pytest matplotlib
```
- Then clone this repository and initialize script:
```
git clone https://github.com/akhilsadam/coe332.git 
cd coe332/homework04/
chmod +rx code/land.py
```
#### Run
- Tester
  - Any tester output without an `AssertionError` is valid.
```
pytest
```
- Run   
  - Replace `<pathtodatafile.json>` with a path to your datafile, or replace `<pathtodatafile.json>` with `data/data.json` to see example output.
```
code/land.py <pathtodatafile.json>
```
#### Build
- If you would like to build a docker container from these files, simply run the following in the repository root directory.
`make build`
- Otherwise, simply run the following, and if the tests pass, the build has suceeded.
```
docker build -t ${NAME}/ml_data_analysis:hw04 .
docker run -it --rm ${NAME}/ml_data_analysis:hw04 pytest code
```


</details>

## Example Output

<details open>
<summary>output for data.json file</summary>

```
Summary for 30 meteors:
 - Average meteor mass = 83857.3g.
 - Hemisphere Distribution:
        Northern & Eastern: 21 meteors.
        Northern & Western: 6 meteors.
        Southern & Eastern: 0 meteors.
        Southern & Western: 3 meteors.
 - Type Distribution:
        L5:             1 meteors.
        H6:             1 meteors.
        EH4:            2 meteors.
        Acapulcoite:    1 meteors.
        L6:             6 meteors.
        LL3-6:          1 meteors.
        H5:             3 meteors.
        L:              2 meteors.
        Diogenite-pm:   1 meteors.
        Stone-uncl:     1 meteors.
        H4:             2 meteors.
        H:              1 meteors.
        Iron-IVA:       1 meteors.
        CR2-an:         1 meteors.
        LL5:            2 meteors.
        CI1:            1 meteors.
        L/LL4:          1 meteors.
        Eucrite-mmict:  1 meteors.
        CV3:            1 meteors.
```

</details>