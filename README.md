# SmaliCompare
<img src="https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=naroSEC&fontSize=90" />
:smiley:기존 Android 앱과 변조된 또는 추가된 Android 앱의 Smali 코드를 비교하여 삭제된 Smali 파일과 변경된 Smali 코드를 쉽고 빠르게 확인할 수 있습니다.

# 활용처
:point_right: Android 디지털 포렌식 CTF 문제 풀이에 활용 할 수 있습니다.<br>
:point_right: 변조된 Android 앱 분석 시 원본 앱과 비교하여 어떤 코드들이 추가 되었는지 빠르게 파악할 수 있습니다.<br>
:point_right: Android 앱 분석 시 이전 버전과 비교하여 어떤 코드들이 추가 되었는지 확인할 수 있습니다.<br>
:point_right: 보안 코드 변경 이력 확인 시에도 유용하게 사용할 수 있습니다.<br>

# 사용 예제
:question: Smali 코드 추출은 <code>"APK Eazy Tool"</code> or <code>apktool</code>을 사용하면 됩니다.

1. 기준이 되는 원본 smali 코드들이 위치한 디렉터리와 변경된 smali 코드들이 위치한 디렉터리를 선택해주세요.
<p>
  <table>
    <tr>
      <td><img src="https://github.com/naroSEC/Anditer/assets/89144246/b1ba0d6f-4cf0-4bf6-96e5-c30574bd9ad3" /></td><td><img src="https://github.com/naroSEC/Anditer/assets/89144246/f61d0c3c-abf6-45cd-9092-43a48d24207e" /></td>
    <tr>
  </table>
</p>

2. 디렉터리 선택이 다 되었다면, 시작 버튼을 클릭해주세요.
<p align="center">
  <img src="https://github.com/naroSEC/Anditer/assets/89144246/668d001f-aae0-44ce-9922-6c6bf6eaf136">
</p>

3. 완료 알림창이 출력되면 파일 비교가 완료된 것으로 YES 버튼을 클릭해주세요.
<p align="center">
  <img src="https://github.com/naroSEC/Anditer/assets/89144246/aadcfff6-270a-4a2b-9f5a-7f3d38ac61cd">
</p>

4. REPORTING.txt 파일을 확인해보면 추가되거나 삭제된 Smali 파일과 변경 이력이 존재하는 클래스 및 함수 정보들을 확인할 수 있습니다.
<p align="center">
  <img src="https://github.com/naroSEC/Anditer/assets/89144246/e0d35930-d8a2-49ee-adcf-d24a6734bd27">
</p>
