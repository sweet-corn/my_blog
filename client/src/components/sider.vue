<!--
 * @Author: your name
 * @Date: 2020-03-17 17:04:44
 * @LastEditTime: 2020-03-18 15:02:16
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /my_blog/client/src/components/sider.vue
 -->
<template>
  <div >
    <Sider hide-trigger :style="{background: '#fff',margin:'0 auto'}">
      <div class="demo-avatar" style="text-align:left">
        <Avatar icon="ios-person" size="100" :src="'http://118.89.125.57/images/'+info.avatar" v-if="info.avatar"/>
        <Avatar icon="ios-person" size="100"  v-else/>
        <div class="text-left"><span class="gray">昵称：</span>{{info.nickName || info.home_id}}</div>
        <div  class="text-left"><span class="gray">性别：</span>{{info.sex || '不男不女'}}</div>
        <div  class="text-left"><span class="gray">来自：</span>{{info.address || '火星'}}</div>
        <div  class="text-left"><span class="gray">签名：</span>{{info.sign || '这家伙太懒 什么也不说...'}}</div>
      </div>
    </Sider>
  </div>
</template>

<script>
export default {
  name: "zSider",
  props: {
    info: {
      type: Object,
      default: {},
    }
  },
  mounted(){
    
  }
};
</script>

<style  scoped>
.demo-avatar>div{
  margin:20px 0;
}
.demo-avatar{
  margin-top:30px;
}
.gray{
  color:#888
}
</style>