# [Silver IV] 데뷔의 꿈 - 24465 

[문제 링크](https://www.acmicpc.net/problem/24465) 

### 성능 요약

메모리: 112152 KB, 시간: 156 ms

### 분류

구현, 정렬

### 제출 일자

2024년 9월 28일 09:37:40

### 문제 설명

<p>7인조 그룹인 Aloha의 새로운 멤버를 뽑는 오디션이 개최되었다. 평소 Aloha의 팬이던 현수는 오디션에 지원하기로 했다.</p>

<p>현수는 1차 서류심사 기준이 기존 멤버들과 별자리가 겹치지 않는 사람이라는 내부정보를 입수했다. 현수는 과연 오디션에 합격할 수 있을까?</p>

<p>아래 별자리표를 참고하여 1차 서류심사를 통과할 수 있는 사람들의 생일을 출력해보자.</p>

<table class="table table-bordered th-center td-center table-center-40">
	<thead>
		<tr>
			<th scope="col">별자리</th>
			<th scope="col">기간</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>물병자리</td>
			<td>1월 20일 ~ 2월 18일</td>
		</tr>
		<tr>
			<td>물고기자리</td>
			<td>2월 19일 ~ 3월 20일</td>
		</tr>
		<tr>
			<td>양자리</td>
			<td>3월 21일 ~ 4월 19일</td>
		</tr>
		<tr>
			<td>황소자리</td>
			<td>4월 20일 ~ 5월 20일</td>
		</tr>
		<tr>
			<td>쌍둥이자리</td>
			<td>5월 21일 ~ 6월 21일</td>
		</tr>
		<tr>
			<td>게자리</td>
			<td>6월 22일 ~ 7월 22일</td>
		</tr>
		<tr>
			<td>사자자리</td>
			<td>7월 23일 ~ 8월 22일</td>
		</tr>
		<tr>
			<td>처녀자리</td>
			<td>8월 23일 ~ 9월 22일</td>
		</tr>
		<tr>
			<td>천칭자리</td>
			<td>9월 23일 ~ 10월 22일</td>
		</tr>
		<tr>
			<td>전갈자리</td>
			<td>10월 23일 ~ 11월 22일</td>
		</tr>
		<tr>
			<td>사수자리</td>
			<td>11월 23일 ~ 12월 21일</td>
		</tr>
		<tr>
			<td>염소자리</td>
			<td>12월 22일 ~ 1월 19일</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫 번째 줄부터 차례로 일곱 명의 Aloha 멤버들의 생일이 한 줄에 하나씩 주어진다.</p>

<p>여덟 번째 줄에는 오디션 지원자의 수 $N$이 주어진다. $(1 \le N \le 10\,000)$</p>

<p>다음 줄부터 $N$개의 줄에는 지원자들의 생일이 한 줄에 하나씩 주어진다. 주어지는 날짜는 유효한 날짜만 주어진다.</p>

<p>모든 생일은 달과 날 순서대로 주어지며 공백으로 구분된다.</p>

### 출력 

 <p>1차 서류심사 합격자들의 생일을 빠른 순서대로 한 줄에 하나씩 출력한다. 합격자가 한 명도 없는 경우 <code>ALL FAILED</code>를 출력한다.</p>

