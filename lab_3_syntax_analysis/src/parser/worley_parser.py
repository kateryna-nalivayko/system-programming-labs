terminals = ['+', '1']
grammar = [['s', ['e']],
           ['e', ['1']],
           ['e', ['e', '+', 'e']]]


class Task:
    def __init__(self, rule, dot, start):
        self.rule = rule
        self.dot = dot
        self.start = start

    def next_symbol(self):
        prod = grammar[self.rule][1]
        return prod[self.dot] if self.dot < len(prod) else None

    def __eq__(self, other):
        return self.rule == other.rule and self.dot == other.dot and self.start == other.start

    def __repr__(self):
        prod = grammar[self.rule][1]
        a = ' '.join(prod[:self.dot])
        b = ' '.join(prod[self.dot:])
        week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        return f'({grammar[self.rule][0]}->{a}.{b}, {week[self.start]})'


def recognize(tokens):
    worklists = [[Task(0, 0, 0)]]

    def add_tasks(i, task):
        if len(worklists) <= i:
            worklists.append([])
        if task not in worklists[i]:
            worklists[i].append(task)

    token_counter = 0
    while True:
        token = next(tokens, None)

        if token_counter == len(worklists):
            return False

        i = 0
        while i < len(worklists[token_counter]):
            task = worklists[token_counter][i]
            next_symbol = task.next_symbol()

            # Completion
            if next_symbol is None:
                for prev in worklists[task.start]:
                    if prev.next_symbol() == grammar[task.rule][0]:
                        add_tasks(token_counter, Task(prev.rule, prev.dot + 1, prev.start))

            # Scanning
            elif next_symbol in terminals:
                if token is not None and next_symbol == token:
                    add_tasks(token_counter + 1, Task(task.rule, task.dot + 1, task.start))

            # Prediction
            else:
                for idx, (lhs, rhs) in enumerate(grammar):
                    if lhs == next_symbol:
                        add_tasks(token_counter, Task(idx, 0, token_counter))

            i += 1

        if token is None:
            break
        token_counter += 1

    # Check for finished grammar
    cur = [task for task in worklists[-1] if task == Task(0, len(grammar[0][1]), 0)]
    print("Worklists:")
    for i, tasks in enumerate(worklists):
        print(f"J{i}: {tasks}")
    return bool(cur)


print(recognize(iter(['1', '+', '1'])))
