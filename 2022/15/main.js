
const fs = require('fs');
const file = fs.readFileSync('input', 'utf-8');
const input = file.split(/(\n)/).filter(m => m.length > 1);

const ROW_SAMPLE = 10;
const LIMIT_SAMPLE = 20;

const ROW_INPUT = 2000000;
const LIMIT_INPUT = 4000000;
const FREQUENCY_MULTIPLIER = 4000000;


function get_map() {
    const map = new Map();
    for (const line of input) {
        const coordinates = line.match(/([-\d]+)/g).map(c => parseInt(c));
        map.set({x: coordinates[0], y: coordinates[1]}, {x: coordinates[2], y: coordinates[3]});
    }
    return map;
}

function get_uncovered_area(map, row) {
    const uncovered_area = new Set();
    for (const [sensor, beacon] of map) {
        const distance = Math.abs(sensor.x - beacon.x) + Math.abs(sensor.y - beacon.y);
        for (let j = sensor.y - distance; j <= sensor.y + distance; j++) {
            if (j == row) {
                for (let i = sensor.x - distance; i <= sensor.x + distance; i++) {
                    if (Math.abs(sensor.x - i) + Math.abs(sensor.y - j) <= distance) {
                        let is_beacon = false;
                        for (const b of map.values()) {
                            if (b.x == i && b.y == j) {
                                is_beacon = true;
                                break;
                            }
                        }

                        if (!is_beacon) {
                            uncovered_area.add(i);
                        }
                    }
                }
            }
        }
    }
    return uncovered_area;
}

function get_tuning_frequency(map, limit, frequency_multiplier) {
    const perimeters = new Map();
    for (const [sensor, beacon] of map) {
        const distance = Math.abs(sensor.x - beacon.x) + Math.abs(sensor.y - beacon.y);
        for (const [s, b] of map) {
            if (s == sensor) {
                continue;
            }

            // diamond shape of sensor
            //                                  (sensor.x, sensor.y - distance)
            //  (sensor.x - distance, sensor.y)                                 (sensor.x + distance, sensor.y)
            //                                  (sensor.x, sensor.y + distance)
            
        }
    }

    /* return beacon.x * frequency_multiplier + beacon.y; */
}

const map = get_map();

//console.log("Uncovered area at row", ROW_INPUT, ":", get_uncovered_area(map, ROW_INPUT).size);
console.log("Tuning frequency:", get_tuning_frequency(map, LIMIT_INPUT, FREQUENCY_MULTIPLIER));
