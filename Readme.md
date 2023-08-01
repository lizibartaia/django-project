# Recipe App

Recipe is an api to create,add,edit or delete recipes.

## Build and run project

Docker is required to run a project

```bash
make build
```
run a project

```bash
make run
```
## Usage
 populate a database with fixture data

```bash
make populate_database
```
create a super user

```bash
make createsuperuser
```
after running a project you shuld be able to perform CRUD operations on the following endpoint:
**localhost:8000/api/recipe**