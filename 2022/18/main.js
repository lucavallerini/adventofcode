
const fs = require('fs');
const file = fs.readFileSync('sample', 'utf-8');

const input = file.split(/(\n)/).filter(m => m.length > 1);

function get_cubes() {
    return input.map(line => line.split(",").map(c => parseInt(c)));
}

function is_cube(cubes, x, y, z) {
    return cubes.find(c => c[0] == x && c[1] == y&& c[2] == z) != undefined;
}

function get_surface_area(cubes) {
    let faces = 0;
    for (const cube of cubes) {
        faces += is_cube(cubes, cube[0] - 1, cube[1], cube[2]) ? 0 : 1;
        faces += is_cube(cubes, cube[0] + 1, cube[1], cube[2]) ? 0 : 1;
        faces += is_cube(cubes, cube[0], cube[1] - 1, cube[2]) ? 0 : 1;
        faces += is_cube(cubes, cube[0], cube[1] + 1, cube[2]) ? 0 : 1;
        faces += is_cube(cubes, cube[0], cube[1], cube[2] - 1) ? 0 : 1;
        faces += is_cube(cubes, cube[0], cube[1], cube[2] + 1) ? 0 : 1;
    }
    return faces;
}

function get_exterior_surface_area(coordinates) {
    const min_x = coordinates.map(c => c[0]).sort((a, b) => a - b)[0];
    const max_x = coordinates.map(c => c[0]).sort((a, b) => a - b).reverse()[0];
    const min_y = coordinates.map(c => c[1]).sort((a, b) => a - b)[0];
    const max_y = coordinates.map(c => c[1]).sort((a, b) => a - b).reverse()[0];
    const min_z = coordinates.map(c => c[2]).sort((a, b) => a - b)[0];
    const max_z = coordinates.map(c => c[2]).sort((a, b) => a - b).reverse()[0];
    console.log(min_x, max_x, min_y, max_y, min_z, max_z);

    const external_cubes = [];
    let external_faces = 0;
    for(let i = min_x; i <= max_x; i++) {
        for(let j = min_y; j <= max_y; j++) {
            // plane xy, moving towards +z
            for(let k = min_z; k <= max_z; k++) {
                if (is_cube(coordinates, i, j, k)) {
                    if (!is_cube(external_cubes, i, j, k)) {
                        external_cubes.push([i, j, k]);
                    }
                    external_faces++;
                    break;
                }
            }

            // plane xy, moving towards -z
            for(let k = max_z; k >= min_z; k--) {
                if (is_cube(coordinates, i, j, k)) {
                    if (!is_cube(external_cubes, i, j, k)) {
                        external_cubes.push([i, j, k]);
                    }
                    external_faces++;
                    break;
                }
            }
        }
    }

    for(let i = min_x; i <= max_x; i++) {
        for(let k = min_z; k <= max_z; k++) {
            // plane xz, moving towards +y
            for(let j = min_y; j <= max_y; j++) {
                if (is_cube(coordinates, i, j, k)) {
                    if (!is_cube(external_cubes, i, j, k)) {
                        external_cubes.push([i, j, k]);
                    }
                    external_faces++;
                    break;
                }
            }

            // plane xz, moving towards -y
            for(let j = max_y; j >= min_y; j--) {
                if (is_cube(coordinates, i, j, k)) {
                    if (!is_cube(external_cubes, i, j, k)) {
                        external_cubes.push([i, j, k]);
                    }
                    external_faces++;
                    break;
                }
            }
        }
    }

    for(let k = min_z; k <= max_z; k++) {
        for(let j = min_y; j <= max_y; j++) {
            // plane yz, moving towards +x
            for(let i = min_x; i <= max_x; i++) {
                if (is_cube(coordinates, i, j, k)) {
                    if (!is_cube(external_cubes, i, j, k)) {
                        external_cubes.push([i, j, k]);
                    }
                    external_faces++;
                    break;
                }
            }

            // plane yz, moving towards -x
            for(let i = max_x; i >= min_x; i--) {
                if (is_cube(coordinates, i, j, k)) {
                    if (!is_cube(external_cubes, i, j, k)) {
                        external_cubes.push([i, j, k]);
                    }
                    external_faces++;
                    break;
                }
            }
        }
    }
    console.log(external_cubes)

    return external_faces;
}

const cubes = get_cubes();
console.log("Surface are:", get_surface_area(cubes));
console.log("Exterior surface are:", get_exterior_surface_area(cubes));
