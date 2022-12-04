
let fs = require('fs');
let file = fs.readFileSync('input', 'utf-8');

let monkeys_input = file.split(/(\n)/).filter(m => m != '\n');
let monkeys_count = monkeys_input.filter(m => m.startsWith('Monkey')).length;
let monkeys_length = monkeys_input.length / monkeys_count;

function init_monkeys() {
    const monkeys = [];
    for (let i = 0; i < monkeys_input.length; i = i + monkeys_length) {
        monkeys.push({
            id: parseInt(monkeys_input[i].match(/([\d]+)/)[0]),
            items: monkeys_input[i+1].split(/([\d]+(,)?)/).filter(v => v && v.match(/([\d]+)/)).map(v => parseInt(v)),
            operation: (old) => eval(monkeys_input[i+2].substring(monkeys_input[i+2].indexOf("=") + 2)),
            multiple_of: parseInt(monkeys_input[i+3].match(/([\d]+)/)),
            test: {
                true: parseInt(monkeys_input[i+4].match(/([\d]+)/)),
                false: parseInt(monkeys_input[i+5].match(/([\d]+)/)),
            },
            inspections: 0,
        });
    }
    return monkeys;
}

function monkey_business(monkeys, rounds, relief_divider) {
    const lcm = monkeys.reduce((acc, m) => acc * m.multiple_of, 1);
    for(let i = 0; i < rounds; i++) {
        monkeys.forEach(monkey => {
            monkey.inspections += monkey.items.length;
            while(monkey.items.length > 0) {
                const item = monkey.items.splice(0, 1)[0];
                const worry_level = Math.floor(monkey.operation(item) / relief_divider) % lcm; // keep worry level manageable
                const to_monkey = monkeys[monkey.test[(worry_level % monkey.multiple_of == 0).toString()]];
                to_monkey.items.push(worry_level);
            }
        });
    }
    monkeys.sort((m1, m2) => m2.inspections - m1.inspections);
    return monkeys[0].inspections * monkeys[1].inspections;
}

const ROUNDS_PART_1 = 20;
const RELIEF_DIVIDER_PART_1 = 3;
console.log("Monkey bussiness 1:", monkey_business(init_monkeys(), ROUNDS_PART_1, RELIEF_DIVIDER_PART_1));

const ROUNDS_PART_2 = 10000;
const RELIEF_DIVIDER_PART_2 = 1;
console.log("Monkey bussiness 2:", monkey_business(init_monkeys(), ROUNDS_PART_2, RELIEF_DIVIDER_PART_2));
