# TMB calculator
##### tumor mutational burden calculation method that works **ONLY** for a custom MGPT (with a given number of sequenced loci)
##### This tool calculates the Tumor Mutational Burden (TMB) from a provided SQLite database. The TMB is calculated as the number of non-synonymous coding variants per megabase (Mb) of the examined sequence.

## about TMB
#### Tumor Mutational Burden (TMB) is an emerging, independent predictive biomarker of immunotherapies in multiple tumor types. It measures the number of mutations within a tumor genome and can offer insight into the likelihood of a patient's response to immunotherapies.

#### The SQLite database should contain a table named variant with at least the following columns:
- base__coding: Indicates whether the variant is coding (with value 'Y') or not.
- base__so: The type of the variant. Non-synonymous coding variants are those that are not of type 'SYN' or 'INT'.


```bash
python tmb_calculator.py [DATABASE_FILE]
```

## Using Docker

### Pulling the Docker Image

Pull the Docker image from the repository:
```
docker pull alperakkus/mutationalburden:latest
```
```
docker run -v /local/path:/data alperakkus/mutationalburden:latest /data/YOUR_DATABASE_FILE.sqlite
```
## 
##### This project is licensed under the MIT License.

