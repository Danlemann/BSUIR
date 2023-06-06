from gluing import *


def calculation_method_sdnf(formula: str):
    new_sdnf = (gluing_sdnf(formula.split('+')))
    a = False
    for i in range(len(new_sdnf)):
        if new_sdnf[i].find('*') == -1:
            a = True
    if not a:
        new_sdnf = check_for_redundant_implications_sdnf(new_sdnf)
    for i in range(len(new_sdnf)):
        new_sdnf[i] = '(' + new_sdnf[i] + ')'
    new_formula = '+'.join(new_sdnf[i] for i in range(len(new_sdnf)))
    return new_formula


def calculation_method_sknf(formula: str):
    new_sknf = check_for_redundant_implications_sknf(gluing_sknf(formula.split('*')))
    a = False
    for i in range(len(new_sknf)):
        if new_sknf[i].find('+') == -1:
            a = True
    if not a:
        new_sknf = check_for_redundant_implications_sdnf(new_sknf)
    for i in range(len(new_sknf)):
        new_sknf[i] = '(' + new_sknf[i] + ')'
    new_formula = '*'.join(new_sknf[i] for i in range(len(new_sknf)))
    return new_formula


def check_for_redundant_implications_sknf(parts: list):

    for m in mints_dec:
        self.mints.append(Minterm(m, num_of_literals))

    for mint in self.mints:
        self.expr += mint.str_value + " + "
        count = 0
        for digit in mint.bin_value:
            if digit == "1":
                count += 1
        group_name = "G" + str(count)
        if not len(self.groups) == 0:
            found = False
            for group in self.groups:
                if group.name == group_name:
                    group.imps.append(Implicant(mint))
                    found = True
            if not found:
                self.groups.append(Group(group_name, Implicant(mint)))
        else:
            self.groups.append(Group(group_name, Implicant(mint)))
    self.expr = self.expr[:-3]


    for group in self.groups:
        group.ones = int(group.name[1:])
    self.groups.sort(key=lambda x: x.ones, reverse=False)

    def combine(self, group1, group2):
        temp_group = Group(group1.name + group2.name)
        for group1_imp in group1.imps:
            for group2_imp in group2.imps:
                if len([i for i in range(self.literals) if group1_imp.bin_value[i] != group2_imp.bin_value[i]]) <= 1:
                    group1_imp.checked = True
                    group2_imp.checked = True
                    temp_group.imps.append(Implicant(group1_imp, group2_imp))

        # should add imp if it is not used in combination
        for imp in group1.imps:
            if not imp.checked:
                temp_group.imps.append(imp)

        # delete duplicate imps
        temp_imps = []
        temp_bin_values = []
        for impl in temp_group.imps:
            temp_imps.append(impl)
            temp_bin_values.append(impl.bin_value)
        temp_bin_values = list(dict.fromkeys(temp_bin_values))
        temp_group.imps.clear()
        for impl in temp_imps:
            if impl.bin_value in temp_bin_values:
                temp_group.imps.append(impl)
                temp_bin_values.remove(impl.bin_value)

        return temp_group

    def solve(self, new_groups):
        count = 0
        for i in range(0, len(new_groups) - 1):
            temp_group = self.combine(new_groups[i], new_groups[i + 1])
            # when to stop?
            if len(temp_group.imps) == len(new_groups[i].imps):  # prevent out of band exception
                same = True
                for k in range(0, len(temp_group.imps)):
                    if not temp_group.imps[k].bin_value == new_groups[i].imps[k].bin_value:
                        same = False
                        break
                if same:
                    count += 1
            new_groups[i] = temp_group

        # the last group
        last_group = new_groups[len(new_groups) - 1]
        temp_last_group = Group(last_group.name)
        for imp in last_group.imps:
            if not imp.checked:
                temp_last_group.imps.append(imp)
        if len(temp_last_group.imps) == 0:  # all imps are combined
            new_groups.remove(last_group)
        else:
            new_groups[len(new_groups) - 1] = temp_last_group  # some of the imps are not combined

        # if groups are not combined any more, then stop; else continue
        if not count >= len(new_groups) - 1:
            self.solve(new_groups)

    def choose(self, left):
        # choice of max minterms
        max_mints = 0
        for mint in left[0].mints:
            if not mint.covered:  # number of not covered minterms
                max_mints += 1
        for imp in left:
            mints_num = 0
            for mint in imp.mints:
                if not mint.covered:
                    mints_num += 1
            if mints_num > max_mints:
                max_mints = mints_num
        choices = []
        for imp in left:
            mints_num = 0
            for mint in imp.mints:
                if not mint.covered:
                    mints_num += 1
            if mints_num == max_mints:
                choices.append(imp)
        # choice of less literal
        choice = choices[0]
        for imp in choices:
            if imp.bin_value.count('-') > choice.bin_value.count('-'):
                choice = imp
        self.optimal_imps.append(choice)

    def optimize(self):
        if not len(self.groups) == 0:
            self.solve(self.groups)
        for group in self.groups:
            for imp in group.imps:
                self.prime_imps.append(imp)

        for mint in self.mints:
            count = 0
            for prime_imp in self.prime_imps:
                if mint in prime_imp.mints:
                    count += 1
            if count == 1:
                for prime_imp in self.prime_imps:
                    if mint in prime_imp.mints and prime_imp not in self.ess_prime_imps:
                        self.ess_prime_imps.append(prime_imp)

        for imp in self.ess_prime_imps:
            self.optimal_imps.append(imp)  # essentials must be in final expression

        left = []
        while True:
            for imp in self.optimal_imps:
                for mint in imp.mints:
                    mint.covered = True
            for mint in self.mints:
                if not mint.covered:  # if some of minterms are not covered
                    for imp in self.prime_imps:
                        if imp not in self.optimal_imps and mint in imp.mints and imp not in left:
                            left.append(imp)
            if not len(left) == 0:
                self.choose(left)
                left.clear()
            else:
                break

        for imp in self.optimal_imps:
            self.optimal_expr += imp.str_value + " + "
        self.optimal_expr = self.optimal_expr[:-3]

    def print_groups(self):
        for group in self.groups:
            print(5 * "-")
            print(group.name)
            for imp in group.imps:
                print(imp.dec_value, "\t", imp.bin_value, "\t", imp.str_value)





def Func(group, variables, PIcount, PI):
    ungrouped = []

    for i in range(0, len(group) - 1):
        for j in range(0, len(group[i])):
            for k in range(0, len(group[i + 1])):
                new_min = ""
                differ = 0
                for bit in range(0, variables):
                    if group[i][j][variables - bit - 1] == group[i + 1][k][
                        variables - bit - 1]:
                        new_min = group[i][j][variables - bit - 1] + new_min
                    else:
                        new_min = "2" + new_min
                        differ += 1
                if new_min not in ungrouped and differ == 1:
                    ungrouped.append(new_min)
                if differ == 1:
                    PIcount[group[i][j]] += 1
                    PIcount[group[i + 1][k]] += 1
                    PIcount[new_min] = 0
                    PI[new_min] = (PI[group[i][j]].union(PI[group[i + 1][k]]))

    group = Grouping(ungrouped, variables)
    return group, PIcount, PI


def is_empty(any):
    if any:
        return False
    else:
        return True


def convert(PI):
    newPI = []
    for i in range(0, len(PI)):
        PIstr = ""
        for j in range(0, len(PI[i][0])):
            if PI[i][0][j] == "2":
                PIstr = PIstr + "-"
            else:
                PIstr = PIstr + PI[i][0][j]
        newPI.append(PIstr)
    return newPI


def solution(input):
    PIcount = {}
    PI = {}
    EPI = []
    NEPI = []
    minterms = GetMintermList(input)
    for i in range(0, len(minterms)):
        PI[minterms[i]] = set([GetNums(minterms)[i]])
        PIcount[minterms[i]] = 0
    variables = len(minterms[0])
    group = Grouping(minterms, variables)
    i = 0
    while group != []:
        group, PIcount, PI = Func(group, variables, PIcount, PI)
        if group == []:
            break
        i += 1
    PI_list = list(PI.items())
    PIcount_list = list(PIcount.items())
    PIs = []
    PI2 = []
    for i in range(0, len(PIcount_list)):
        if PIcount_list[i][1] == 0:
            PIs.append((PI_list[i][0]))
            PI2.append(set(PI_list[i][1]))
            if len(PI2) == 1:
                EPI.append(PI_list[i])
            else:
                for j in range(0, len(PI2)):
                    checker = 0
                    target = PI2[j]
                    for k in range(0, len(PI2)):
                        if is_empty(target - PI2[k]):
                            if target == PI2[k]:
                                pass
                            else:
                                checker += 1
                        else:
                            checker += 1
                    if checker == 1:
                        if PI_list[i] not in EPI:
                            EPI.append(PI_list[i])
                    else:
                        if PI_list[i] not in NEPI:
                            NEPI.append(PI_list[i])

    newEPI = convert(EPI)
    newNEPI = convert(NEPI)
    answer = []
    answer.append("EPI")
    if newEPI:
        for i in range(0, len(newEPI)):
            answer.append(newEPI[i])
    answer.append("NEPI")
    if newNEPI:
        for i in range(0, len(newEPI)):
            answer.append(newNEPI[i])
    return answer

