def main():
    altitude_lis = []
    for i in range(10):
        input_line = raw_input()
        altitude = int(input_line)
        altitude_lis.append(altitude)
        
    altitude_lis.sort()
    altitude_lis.reverse()
    for i in range(3):
        print(altitude_lis[i])
        
if __name__ == '__main__':
    main()