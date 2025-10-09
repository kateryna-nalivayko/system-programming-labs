from dataclasses import dataclass
from typing import Iterable, List, Any

DEFAULT_TERMINALS = ['+', '1']
DEFAULT_GRAMMAR = [
    ['s', ['e']],
    ['e', ['1']],
    ['e', ['e', '+', 'e']],
]


@dataclass(eq=True, frozen=True)
class Task:
    rule: int
    dot: int
    start: int


class EarleyParser:
    def __init__(self, terminals=None, grammar=None, debug: bool = False):
        self.terminals = set(terminals or DEFAULT_TERMINALS)
        self.grammar = grammar or DEFAULT_GRAMMAR
        self.debug = debug
        self.chart: List[List[Task]] = []
        self.tokens: List[Any] = []

    def _rhs(self, rule_idx: int) -> List[str]:
        return self.grammar[rule_idx][1]

    def _lhs(self, rule_idx: int) -> str:
        return self.grammar[rule_idx][0]

    def _add_task(self, i: int, task: Task) -> None:
        while len(self.chart) <= i:
            self.chart.append([])
        if task not in self.chart[i]:
            self.chart[i].append(task)

    def recognize(self, tokens: Iterable[Any]) -> bool:
        self.chart = [[Task(0, 0, 0)]]
        self.tokens = list(tokens)

        pos = 0
        while True:
            token = self.tokens[pos] if pos < len(self.tokens) else None

            if pos == len(self.chart):
                return False

            i = 0
            while i < len(self.chart[pos]):
                task = self.chart[pos][i]
                rhs = self._rhs(task.rule)
                next_sym = rhs[task.dot] if task.dot < len(rhs) else None

                if next_sym is None:
                    # Completion: A→α.
                    A = self._lhs(task.rule)
                    for prev in self.chart[task.start]:
                        prev_rhs = self._rhs(prev.rule)
                        prev_next = prev_rhs[prev.dot] if prev.dot < len(prev_rhs) else None
                        if prev_next == A:
                            self._add_task(pos, Task(prev.rule, prev.dot + 1, prev.start))

                elif next_sym in self.terminals:
                    # Scanning
                    if token is not None and token == next_sym:
                        self._add_task(pos + 1, Task(task.rule, task.dot + 1, task.start))

                else:
                    # Prediction
                    for idx, (lhs, rhs2) in enumerate(self.grammar):
                        if lhs == next_sym:
                            self._add_task(pos, Task(idx, 0, pos))

                i += 1

            if token is None:
                break
            pos += 1

        goal_len = len(self._rhs(0))
        goal = any(t.rule == 0 and t.dot == goal_len and t.start == 0 for t in self.chart[-1])

        if self.debug:
            self.pretty_print_chart()
        return goal

    def pretty_print_chart(self) -> None:
        week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

        def fmt(task: Task) -> str:
            rhs = self._rhs(task.rule)
            a = ' '.join(rhs[:task.dot])
            b = ' '.join(rhs[task.dot:])
            return f'({self._lhs(task.rule)}->{a}.{b}, {week[task.start % 7]})'

        print('Worklists:')
        for j, tasks in enumerate(self.chart):
            print(f'J{j}: [' + ', '.join(fmt(t) for t in tasks) + ']')


if __name__ == '__main__':
    parser = EarleyParser(debug=True)
    print(parser.recognize(['1', '+', '1']))
