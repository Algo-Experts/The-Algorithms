## JAVASCRIP CRASH START

### 1. 기본

자바 스크립트는 본래 각 브라우저에 해당하는 엔진에 의해서 구동되는 것이 원칙이다. 대표적으로는 google 의 chrome 에서 구동되는 v8 엔진이 대표적인데, v8 엔진에 의해 만들어진 것이
node.js 이다. 더 디테일한 설명이 추가되면 좋겠지만 (JIT 이라던지 등등), 일단 현재로써는 node.js 를 통해서 브라우저가 아닌 local ide 에서도 js code 가 구동이 될 수 있도록 만들어주는 것이 node js 이다.

아무튼 vscode ide 에서 js code 를 마치 브라우저에서 수행 하는 것처럼 사용하기 위해서는 node 가 깔려 있어야 하며, nodemon 이나 quoakka 였나? vscode marketplace 에서 install 해서 작업하면 훨씬 좋다.

```zsh

node -v
# 버전 확인

node solution.js

or

nodemon solution.js --> 이걸 추천

```
