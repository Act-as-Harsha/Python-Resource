from collections import defaultdict

def count_atoms(formula):
    def parse():
        count = defaultdict(int)
        while self.i < len(formula):
            if formula[self.i] == '(':
                self.i += 1
                inner = parse()
                num = read_number()
                for atom in inner:
                    count[atom] += inner[atom] * num
            elif formula[self.i] == ')':
                self.i += 1
                return count
            else:
                name = read_name()
                num = read_number()
                count[name] += num
        return count

    def read_name():
        start = self.i
        self.i += 1
        while self.i < len(formula) and formula[self.i].islower():
            self.i += 1
        return formula[start:self.i]

    def read_number():
        if self.i >= len(formula) or not formula[self.i].isdigit():
            return 1
        start = self.i
        while self.i < len(formula) and formula[self.i].isdigit():
            self.i += 1
        return int(formula[start:self.i])

    self = type('', (), {})()
    self.i = 0
    result = parse()
    return dict(sorted(result.items()))

user_formula = input("Enter a chemical formula: ")
atom_counts = count_atoms(user_formula)

print("\nAtom counts:")
for atom, count in atom_counts.items():
    print(f"{atom}: {count}")
