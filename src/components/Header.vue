<template>
	<div class="header">
		<div class="logo"><p id="top">랜덤BTS</p></div>
		<div class="kor intro">
			<p>당신을 위한</p>
			<p>BTS 가사 랩을</p>
			<p>만들어줍니다.</p></div>
		<div class="eng intro">
			<p>WE MAKE</p>
			<p>BTS RAPS</p>
			<p>FOR YOU</p></div>
	</div>
</template>
<script>
	export default {

	}
</script>
<style lang="scss">

.header{
	font-family: 'Typo_SsangmunDong';
	margin:0px;
	top:0px;
	position:fixed;
	z-index:9999;
	text-align: left;
}

p{
	margin:0px;
}
#top{
	height:80px;
    display: table-cell;
    vertical-align: middle;
}

.logo{
	display: inline-block;
	padding:0px;
	margin-left:20px;
	margin-right:50px;
	font-size:20px;
}

.intro{
	display: inline-block;
	padding:0px;
	margin:20px;
	margin-right:50px;
	font-size:16px;
}

</style>
