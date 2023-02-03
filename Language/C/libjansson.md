
### 개요
C언어에서 JSON Object 형식을 다룰 수 있도록 해주는 API

### API
json_object_new_object 
- json object 메모리를 할당
- 
json_object_object_add 
- dataobj에 키&값을 넣어줍니다
- 데이터 값을 넣어줄 때에는 자료형에 맞는 함수를 호출해야 합니다
- 
json_tokener_parse()
- 읽어들인 JSON type의 데이터를 파싱한다.
- json_tokener_parse()를 통해 데이터를 파싱하고 파싱된 데이터를 각각의 json_object에 매칭 시킨 후에 데이터를 추출

json_object_object_get()
- JSON type의 데이터에서 object를 추출한다.
- 실제 데이터를 읽기 위해서는 먼저 object에 원하는 필드를 할당하고 해당 필드를 읽으면 된다. 
- 각 데이터 type로 json_object_get_int(), json_object_get_double(), json_object_get_boolean()등도 있다.

json_object_get_int()
- json object에서 정수값을 추출한다.

json_object_get_string()
- json object에서 string값을 추출한다.

json_object_array_get_idx()
- array type의 json object에서 값을 추출한다.
-  array type의 테이터는 json_object_array_length()를 통해 데이터의 길이를 가져온 후에json_object_array_get_idx()를 사용해서 순차적으로 데이터를 읽어 들이면 된다.

int json_dump_file(const json_t *json, const char *path, size_t flags)
- json object를 path에 지정된 파일로 출력

json_t *json_load_file(const char *path, size_t flags, json_error_t *error)
- json object를 path에 지정된 경로에서 가져옴.

json_decref(main_obj);
- 입력된 json object를 하위 루틴을 순차적으로 돌면서 할당된 object를 free함.

### 참조링크
예제 1
https://developmentlee.tistory.com/39
예제 2
https://codinghero.tistory.com/176
예제 3
https://indienote.tistory.com/346