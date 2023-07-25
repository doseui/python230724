import csv

def mode_change_times(input_file):
    mode_changes = []
    with open(input_file, 'r', newline='') as file:
        # csv.DictReader를 사용하여 헤더가 있는 입력 파일을 읽음
        reader = csv.DictReader(file, delimiter='\t')

        prev_mode = None
        for row in reader:
            # 현재 행에서 'Time', 'Mode', 'Status' 값을 추출
            time, mode, _ = row['Time'], int(row['Mode']), int(row['Status'])

            # Mode가 7780에서 7712로 변경되는지 확인
            if prev_mode is not None and mode != prev_mode:
                if mode == 7712 and prev_mode == 7780:
                    mode_changes.append(time)
            prev_mode = mode

    return mode_changes

def convert_status_to_hex(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        # csv.DictReader를 사용하여 헤더가 있는 입력 파일을 읽음
        reader = csv.DictReader(infile, delimiter='\t')

        # csv.writer를 사용하여 탭으로 구분된 값으로 출력 파일에 작성
        writer = csv.writer(outfile, delimiter='\t')

        for row in reader:
            # 현재 행에서 'Time', 'Mode', 'Status' 값을 추출
            time, _, status = row['Time'], row['Mode'], int(row['Status'])

            # Status를 16진수로 변환하고 '0x' 접두사 제거
            status_hex = hex(status)[2:]

            # 시간과 상태 16진수 값을 출력 파일에 작성
            writer.writerow([time, status_hex])

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    # 작업 1: Mode가 7780에서 7712로 변경되는 시간 찾기
    mode_changes = mode_change_times(input_file)
    print("Mode가 7780에서 7712로 변경된 시간:", mode_changes)

    # 작업 2: Status를 16진수로 변환하여 새 파일 생성
    convert_status_to_hex(input_file, output_file)
    print(f"출력이 {output_file}에 작성되었습니다.")