<template>
  <div class="todo">
    <h1>This is an Todo page</h1>
    <v-simple-table dark height="300px">
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">タイトル</th>
            <th class="text-left">内容</th>
            <th class="text-left">投稿時間</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="todo in todos" :key="todo.id">
            <td>{{ todo.id }}</td>
            <td>{{ todo.title }}</td>
            <td>{{ todo.content }}</td>
            <td>{{ todo.created_at }}</td>
          </tr>
        </tbody>
      </v-simple-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    todos: []
  }),
  mounted() {
    this.getApi();
  },
  methods: {
    getApi() {
      axios.get(process.env.VUE_APP_ROOT_API + "todos/").then(response => {
        this.todos = response.data;
      });
    }
  }
};
</script>
