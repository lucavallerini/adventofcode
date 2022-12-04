
const fs = require('fs');
const file = fs.readFileSync('input', 'utf-8');

const input = file.split(/(\n)/).filter(m => m.length > 1);

function get_messages() {
    return input.map(m => eval(m));
}

function compare_messages(left, right) {
    if (Number.isInteger(left) && Number.isInteger(right)) {
        return left < right ? -1 : left == right ? 0 : 1;
    } else if (Array.isArray(left) && Array.isArray(right)) {
        for (let i = 0; i < left.length; i++) {
            if (i < right.length) {
                const result = compare_messages(left[i], right[i]);
                if ( result == 1 ) {
                    // Right side is smaller, so inputs are NOT in the right order
                    return 1;
                } else if ( result == -1 ) {
                    // Left side is smaller, so inputs are in the right order
                    return -1;
                }
            } else {
                // Right side ran out of items, so inputs are NOT in the right order
                return 1;
            }
        }

        if ( left.length < right.length ) {
            // Left side ran out of items, so inputs are in the right order
            return -1;
        }

        // No decision
        return 0;
    } else if (Number.isInteger(left)) {    
        // Mixed types, convert left to [left]
        return compare_messages([left], right);
    } else {
        // Mixed types, convert right to [right]
        return compare_messages(left, [right]);
    }
}

function find_in_order_messages_sum() {
    const messages = get_messages();
    const in_order_messages = [];
    for (let i = 0; i < messages.length; i += 2) {
        if (compare_messages(messages[i], messages[i+1]) == -1) {
            in_order_messages.push(i/2+1);
        }
    }
    return in_order_messages.reduce((accIn, value) => accIn + value, 0);
}

function get_decoder_key() {
    const DIVIDER_PACKET_1 = [[2]];
    const DIVIDER_PACKET_2 = [[6]];

    const messages = get_messages();
    messages.push(DIVIDER_PACKET_1, DIVIDER_PACKET_2);
    messages.sort(compare_messages);

    return (messages.indexOf(DIVIDER_PACKET_1) + 1) * (messages.indexOf(DIVIDER_PACKET_2) + 1);
}

console.log("Sum of in order messages indexes:", find_in_order_messages_sum());
console.log("Decoder key:", get_decoder_key());
