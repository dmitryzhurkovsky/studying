<template>
  <div class="post" v-if="posts.length > 0">
    <h3>List of posts</h3>
    <transition-group name="post-list">
      <post-item
          v-for="post in posts"
          :post="post"
          :key="post.id"
          @remove="$emit('remove', post)"
      ></post-item>
    </transition-group>

  </div>
  <div v-else>
    <h3>List of posts is empty.</h3>
  </div>
</template>

<script>
import PostItem from "@/components/postItem";

export default {
  components: {PostItem},
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.post-list-item {
  display: inline-block;
  margin-right: 10px;
}

.post-list-enter-active,
.post-list-leave-active {
  transition: all 0.3s ease;
}

.post-list-enter-from,
.post-list-leave-to {
  opacity: 0;
  transform: translateX(130px);
}
/*Class is responsible for sorted*/
.post-list-move {
  transition: transform 0.3s ease;
}
</style>