# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

코딩 테스트 알고리즘 풀이 저장소. 주로 Python과 일부 Java로 작성된 문제 풀이 모음.

## 구조

- **Programmers/**: 프로그래머스 문제 풀이 (level1~level3으로 분류)
- **ThisIsCodingTest/**: "이것이 코딩 테스트다" 교재 풀이 (Part2: Greedy, Implementation, DFS/BFS)
- **Codility/**: Codility 문제 풀이
- **Kakaoenter_codingTest/**: 카카오엔터 코딩테스트 풀이

## 언어

- Python (주 언어) — 별도 빌드/테스트 프레임워크 없이 개별 스크립트로 실행
- Java (일부) — `Programmers/level1/공원.java`, `Programmers/level2/충돌위험찾기.java`

## 실행 방법

```bash
# Python 풀이 실행
python3 "Programmers/level1/K번째수.py"

# Java 풀이 컴파일 및 실행
javac "Programmers/level2/충돌위험찾기.java"
java -cp Programmers/level2 Solution
```

## 파일 네이밍 규칙

- 파일명은 문제 제목(한글) 그대로 사용 (예: `가운데 글자 가져오기.py`)
- 난이도별 디렉토리로 분류
