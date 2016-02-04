def hanoi_towers(disk, start, end, middle):
    if disk > 0:
        hanoi_towers(disk - 1, start, middle, end)
        # Move the N disk
        print('Move disk' + str(disk) + ' from ' + start + ' to ' + end)
        hanoi_towers(disk - 1, middle, end, start)

if __name__ == '__main__':
    hanoi_towers(int(input('how many disk?: ')), 'start', 'end', 'middle')
