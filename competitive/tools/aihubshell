#!/bin/bash

echo "=========================================="
echo "aihubshell version 25.09.19 v0.6"
echo "=========================================="

# 상수정의
VER="0.6"
BASE_URL="https://api.aihub.or.kr"
LOGIN_URL="$BASE_URL/api/keyValidate.do"
BASE_DOWNLOAD_URL="$BASE_URL/down/$VER"
MANUAL_URL="$BASE_URL/info/api.do"
BASE_FILETREE_URL="$BASE_URL/info"
DATASET_URL="$BASE_URL/info/dataset.do"
DATAPCKAGE_URL="$BASE_URL/info/datapckage.do"
BASE_PCKAGETREE_URL="$BASE_URL/info/pckage"
BASE_PCKAGE_DOWNLOAD_URL="$BASE_URL/down/pckage/$VER"

# 사용법 출력 함수
print_usage() {
    manual=$(curl -s "$MANUAL_URL")
    # echo -e "$manual"

    echo $manual | grep -oP '"SJ":"\K[^"]+' | head -n 1
    echo -e '\n'
    # 제목 출력
    echo -e "COMMAND\t\t OPTION\t\t\t\t DETAIL"

    # 데이터 처리 및 출력
    echo "$manual" | awk -F'"' -v RS='},' '
    /ENGL_CMGG/ && /KOREAN_CMGG/ && /DETAIL_CN/ {
        for(i=1; i<=NF; i++) {
            if($i == "ENGL_CMGG") engl=$(i+2)
            if($i == "KOREAN_CMGG") korean=$(i+2)
            if($i == "DETAIL_CN") {
                detail=$(i+2)
                gsub(/\\n/, "\n", detail)
                gsub(/\\t/,"\t\t", detail)
                gsub(/\\/,"", detail)
            }
        }
        printf "%-10s\t %-15s\t|\t %s\n\n", engl, korean, detail
    }'
}

# -help 파라미터가 있는 경우 사용법 출력
if [[ "$1" == "-help" ]]; then
    print_usage
    exit 0
fi

# 파라미터 파싱
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -aihubapikey) aihubapikey="$2"; shift ;;
        -mode) 
            mode="$2";
            # 만약 mode가 'l'이고 다음 값이 숫자인 경우 datasetkey로 설정
            if [[ "$mode" == "l" ]]; then
                if [[ "$3" =~ ^[0-9]+$ ]]; then
                    datasetkey="$3";
                    shift;
                fi
            elif [[ "$mode" == "pl" ]]; then
                echo "mode is pl. is it?? mode ::: $mode" ;
                if [[ "$3" =~ ^[0-9]+$ ]]; then
		    datapckagekey="$3";
		    shift;
		fi    
	    fi
            shift;
            ;;
        -datasetkey) datasetkey="$2"; 
		shift ;;
        -filekey) filekeys="$2"; 
		shift ;;
        -datapckagekey) datapckagekey="$2"; 
		shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# mode가 'd'인 경우 datasetkey가 필수값인지 체크
if [[ "$mode" == "d" && -z "$datasetkey" ]]; then
    echo "Error: datasetkey is required when mode is 'd'";
    exit 1;
elif [[ "$mode" == "pd" && -z "$datapckagekey" ]]; then
    echo "Error: datapckagekey is required when mode is 'pd'";
    exit 1;
fi

# 환경 변수에서 아이디와 패스워드 읽어오기 (파라미터가 제공되지 않은 경우에만)
aihubapikey=${aihubapikey:-$AIHUB_APIKEY}
filekeys=${filekeys:-"all"}

# 기존 다운로드 파일 삭제
cleanup() {
    if [ -e "download.tar" ]; then
    	rm "download.tar"
    	echo -e "\n다운로드가 중단되었습니다."
    fi
    exit 1          
}

# 다운로드
down_func() {
	local DOWN_URL="$1";
	
	# 상세한 출력을 화면에 표시하면서 다운로드를 진행합니다.
	http_response=$(curl -L -C - -o "download.tar" -H "apikey:$aihubapikey" -w "\n%{http_code}" "$DOWN_URL?fileSn=$filekeys")
	http_status=$(echo "$http_response" | tail -n1)
	http_body=$(echo "$http_response" | sed '$d')
	
	# HTTP 상태에 따른 처리를 수행합니다.
    if [ "$http_status" -eq 200 ]; then
	echo "Request successful with HTTP status $http_status."
	# curl 명령의 종료 코드를 확인합니다.
	curl_exit_code=$?
		
        if [ $curl_exit_code -eq 0 ]; then
            echo "Download successful."
            # tar 파일을 해제
            tar -xvf download.tar

            echo '잠시 기다려 주세요 병합중 입니다. '
                merge_parts() {
                    local target_dir="$1"
                    
                    # 해당 폴더에 있는 모든 part 파일들의 prefix를 찾음
                    for prefix in $(ls "$target_dir" | grep '.*\.part[0-9]*$' | sed 's/\(.*\)\.part[0-9]*$/\1/' | sort -u); do
                    	# 파일명에 있는 특수문자 이스케이프 처리
                        escaped_prefix=$(printf '%q' "$prefix")
                        
                        echo "Merging $prefix in $target_dir"
                        
                        # 찾은 prefix로 시작하는 모든 part 파일들을 알파벳순으로 정렬하여 병합
                        #cat "${target_dir}/${prefix}".part* > "${target_dir}/${prefix}"
                        find "${target_dir}" -name "${escaped_prefix}.part*" -print0 | sort -zt'.' -k2V | xargs -0 cat > "${target_dir}/${prefix}" 
                        
                        # 병합이 완료된 후 part 파일들을 삭제
                        rm "${target_dir}/${prefix}".part*
                    done
                }

                # 모든 하위 폴더를 탐색하며 마지막 자식 폴더인 경우에 merge_parts 함수 호출
                find . -type d | while read -r dir; do
                    if [[ ! -z $(find "$dir" -maxdepth 1 -name '*.part*') ]]; then
                        merge_parts "$dir"
                    fi
                done

                echo '병합이 완료 되었습니다. '
                rm download.tar
            else
	    echo "Download failed with curl exit code $curl_exit_code."
        fi

    else
        echo "Download failed with HTTP status $http_status."
        echo "Error msg:" 
            cat download.tar
            rm download.tar
    fi
}

# mode에 따른 로직 수행
case $mode in
    d)
        trap cleanup SIGINT		

        if [ -e "download.tar" ]; then
	    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    	    mv "download.tar" "download_$TIMESTAMP.tar"
    	    echo "msg : download.tar 파일이 존재하여 download_$TIMESTAMP.tar로 백업하였습니다."
        fi
        # filekeys 값을 사용하여 요청 전송 및 zip 다운로드
        DOWNLOAD_URL="$BASE_DOWNLOAD_URL/$datasetkey.do"
            
	    down_func $DOWNLOAD_URL
        ;;
    l)
        if [[ $datasetkey ]]; then
            # 파일 트리 구조 요청 및 출력
            FILETREE_URL="$BASE_FILETREE_URL/$datasetkey.do"
            echo "Fetching file tree structure..."
            file_tree=$(curl -s "$FILETREE_URL")
            echo "$file_tree"
        else
            # 데이터셋 조회
            echo "Fetching dataset information..."
            dataset_info=$(curl -s "$DATASET_URL")
            echo "$dataset_info"
        fi
        ;;
    pl)
        echo "mode pl start!!"
		if [[ $datapckagekey ]]; then
		    # 파일 트리 구조 요청 및 출력
		    PCKAGETREE_URL="$BASE_PCKAGETREE_URL/$datapckagekey.do"
		    echo "Fetching datapckage file tree structure..."
		    pckage_tree=$(curl -s "$PCKAGETREE_URL")
		    echo "$pckage_tree"
		else 
		    # 데이터 패키지 조회
		    echo "Fetching datapckage information..."
		    datapckage_info=$(curl -s "$DATAPCKAGE_URL")
		    echo "$datapckage_info"
		fi	
        ;;
    pd)
		trap cleanup SIGINT
		
		if [ -e "download.tar" ]; then
	    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    	    mv "download.tar" "download_$TIMESTAMP.tar"
    	    echo "msg : download.tar 파일이 존재하여 download_$TIMESTAMP.tar로 백업하였습니다."
        fi
        
        PCKAGE_DOWNLOAD_URL="$BASE_PCKAGE_DOWNLOAD_URL/$datapckagekey.do"
        #echo "PCKAGE_DOWNLOAD_URL ::::::::::::::::::: $PCKAGE_DOWNLOAD_URL";
        down_func $PCKAGE_DOWNLOAD_URL
        ;;
    *)
        echo "Invalid mode. Please use 'pd','pl' for datapckage list,'d', 'l' for dataset list, 'l [datasetkey]' for file tree"
        exit 1
        ;;
esac



