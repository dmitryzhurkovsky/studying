<template>
  <div class="app">
    <my-dialog v-model:show="dialogVisible">
      <post-form @create="createPost"></post-form>
    </my-dialog>
    <h1>Posts page</h1>
    <my-input
        v-model="searchQuery"
        placeholder="Search ..."
    />
    <div class="app__btns">
      <my-button
          @click="showDialog"
      >
        Create post
      </my-button>
      <my-select
          v-model="selectedSort"
          :options="sortOptions"
      />
    </div>
    <post-list
        :posts="sortedAndSearchPosts"
        @remove="removePost"
        v-if="!isPostsLoading"
    >
    </post-list>
    <div v-else>Loading posts...</div>
    <!--    <div class="page__wrapper">-->
    <!--      <div-->
    <!--          v-for="pageNumber in totalPages"-->
    <!--          :key="pageNumber"-->
    <!--          class="page"-->
    <!--          :class="{-->
    <!--            // The same way you can bind styles.-->
    <!--            // key - название класса, значение - какое-то логическое условие-->
    <!--            'current-page': page === pageNumber-->
    <!--          }"-->
    <!--          @click="changePage(pageNumber)"-->
    <!--      >-->
    <!--        {{ pageNumber }}-->
    <!--      </div>-->
    <!--    </div>-->

    <!--    Check it's the end of page?-->
    <div ref="observer" class="observer"></div>
  </div>
</template>

<script>
import postForm from '@/components/postForm';
import postList from '@/components/postList';
import axios from 'axios';

export default {
  components: {
    postForm,
    postList
  },
  data() {
    return {
      posts: [],
      dialogVisible: false,
      isPostsLoading: false,
      selectedSort: '',
      searchQuery: '',
      page: 1,
      limit: 10,
      totalPages: 0,
      sortOptions: [
        {value: 'title', name: 'By title'},
        {value: 'body', name: 'by body'}
      ]
    }
  },
  methods: {
    createPost(post) {
      this.posts.push(post);
      this.dialogVisible = false;
    },
    removePost(post) {
      this.posts = this.posts.filter(p => p.id !== post.id)
    },
    showDialog() {
      this.dialogVisible = true
    },
    // changePage(pageNumber) {
    //   this.page = pageNumber;
    //   // this.fetchPosts() - comment to practise watch property, See watch property.
    // },
    async fetchPosts() {
      try {
        this.isPostsLoading = true;
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
          params: {
            _page: this.page,
            _limit: this.limit
          }
        });
        // Округдение в большую сторону - Math.ceil.
        this.totalPages = Math.ceil(response.headers['x-total-count'] / this.limit);
        this.posts = response.data;
      } catch (e) {
        alert('Error')
      } finally {
        this.isPostsLoading = false;
      }
    },
    async LoadMorePosts() {
      try {
        this.page += 1
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
          params: {
            _page: this.page,
            _limit: this.limit
          }
        });
        // Округдение в большую сторону - Math.ceil.
        this.totalPages = Math.ceil(response.headers['x-total-count'] / this.limit);
        this.posts = [...this.posts, ...response.data];
      } catch (e) {
        alert('Error')
      }
    }
  },
  mounted() {
    this.fetchPosts();
    //  Functional for infinity scrolling:
    console.log(this.$refs.observer)
    const options = {
      rootMargin: '0px',
      threshold: 1.0
    }
    const callback = (entries, observer) => {
      if (entries[0].isIntersecting && this.page < this.totalPages) {
        this.LoadMorePosts()
      }
    };
    const observer = new IntersectionObserver(callback, options);
    observer.observe(this.$refs.observer);
  },
  computed: {
    sortedPost() {
      // Всегда должна что-то возвращать. Кэшируют результат вычисления функции, сделает переасчет только тогда, когда
      // изменится зависимость.
      return [...this.posts.sort((post1, post2) => {
        return post1[this.selectedSort]?.localeCompare(post2[this.selectedSort])
      })]
    },
    sortedAndSearchPosts() {
      return this.sortedPost.filter(post => post.title.toLowerCase().includes(this.searchQuery.toLowerCase()))
    }
  },
  watch: {
    // page() {
    //   // 2 way to resolve this task is in methods -> changePage
    //   this.fetchPosts()
    // }
    //   // Наблюдаемая функция
    //   // Функция наблюдатель должна иметь такое же название как и моделька. Параметр принимаемая - значение, на которое
    //   // была изменена моделька
    //   selectedSort(newValue) {
    //     this.posts.sort((post1, post2) => {
    //       return post1[newValue]?.localeCompare(post2[newValue])
    //     })
    //   },
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  padding: 20px;
}

.app__btns {
  margin: 15px 0;
  display: flex;
  justify-content: space-between;
}


.page__wrapper {
  display: flex;
  margin-top: 15px;
}

.page {
  border: 1px solid black;
  padding: 10px;
}

.current-page {
  border: 2px solid teal;
}

.observer {
  height: 30px;
  background: greenyellow;
}
</style>