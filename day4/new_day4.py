enable_debug = False


def debug(string):
    if enable_debug:
        print(string)


class Passport:

    def __init__(self):
        self.passports = []

    def serialize_string(self, raw_string):
        item = raw_string.split(':')
        return item[0], item[1]


    def readfile(self, filepath):
        f = open(filepath, 'r')
        lines = f.readlines()

        raw_passport = {}
        for line in lines:
            if not line.strip():
                self.passports.append(raw_passport)
                raw_passport = {}
                continue
            items = line.split(' ')
            for item in items:
                key, value = self.serialize_string(item)
                raw_passport[key] = value.replace('\n', '')
        self.passports.append(raw_passport)

        print(f'Got {len(self.passports)} new passports!')
    
    def check_validity(self):
        valid_passports = 0
        num_of_check = 0

        for passport in self.passports:
            byr = passport.get('byr')
            iyr = passport.get('iyr')
            eyr = passport.get('eyr')
            hgt = passport.get('hgt')
            hcl = passport.get('hcl')
            ecl = passport.get('ecl')
            pid = passport.get('pid')
            cid = passport.get('cid')

            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                if not (1920 <= int(byr) <= 2002):
                    debug(f'1920 < {byr} < 2002')
                    continue

                if not (2010 <=int(iyr) <= 2020):
                    debug(f'2010 < {iyr} < 2020')
                    continue

                if not (2020 <= int(eyr) <= 2030):
                    debug(f'2020 < {eyr} < 2030')
                    continue

                if not 'in' in hgt and not 'cm' in hgt:
                    debug(f'"in" or "cm" missing: {hgt}')
                    continue

                if 'in' in hgt:
                    hgt = hgt.replace('in', '')
                    if not (59 <= int(hgt) <= 76):
                        debug(f'59 < {hcl} < 76')
                        continue

                if 'cm' in hgt:
                    hgt = hgt.replace('cm', '')
                    if not (150 <= int(hgt) <= 193):
                        debug(f'150 < {hcl} < 193')
                        continue

                if not hcl[0] == '#':
                    debug(f'hcl doesnt start with #: {hcl}')
                    continue

                if not len(hcl) == 7:
                    debug(f'hcl length wrong: {len(hcl)}, {hcl}')
                    continue

                for char in hcl[1:]:
                    if not char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                        debug(f'hcl has invalid chars: {hcl}')
                        continue

                if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    debug(f'ecl not in list: {ecl}')
                    continue

                if not len(pid) == 9:
                    debug(f'pid length is wrong: {len(pid)}, {pid}')
                    continue

                valid_passports += 1
            else:
                debug(f'{not byr} {not iyr} {not eyr} {not hgt} {not hcl} {not ecl} {not pid}')

        return valid_passports
        

passport = Passport()
passport.readfile('input.txt')
print(passport.check_validity())
