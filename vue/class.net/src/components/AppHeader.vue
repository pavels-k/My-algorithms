<template>
  <v-app id="inspire">
    
    <v-content>
 
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="start"
          justify="start"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="pa-2"
            outlined
            tile>
              <v-toolbar
                color="blue"
                dark
                flat
              >
                <v-toolbar-title>Форма авторизации</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Логин"
                    name="login"
                    prepend-icon="person"
                    type="text"
                  />

                  <v-text-field
                    id="password"
                    label="Пароль"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  />
                  
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn color="blue " dark block = True>Войти</v-btn>
                
              </v-card-actions>
              <v-card-actions>
                <v-spacer />
                <v-btn color="blue" dark block = True>Регистарция</v-btn>
                
              </v-card-actions>
              
            </v-card>
            
            
          </v-col>
          <v-col>
          <div>
         
  <p>В состав комплекса CLASS.NET входит:</p>
	<div class="box">
		<ul>
			<li> блоки задач:
				<ul>
					<li> тестирующие,</li>
					<li> самообучающие,</li>
					<li> контролирующие;</li>
				</ul>
			</li>
			<li> раздел статистики решения задач;</li>
			<li> раздел статистики по факультету и система рейтингов;</li>
			<li>для преподавателей:
				<ul>
					<li> возможности администрирования группы,</li>
					<li> просмотр статистики решения задач по группе.</li>
				</ul>
			</li>
		</ul>
	</div>
  </div>
        </v-col>
        </v-row>
      </v-container>
    </v-content>



    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Главная страница</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-format-list-text</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Теория</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Практика</v-list-item-title>
          </v-list-item-content>
        </v-list-item>



      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="blue"
      dark
    >
    
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Меню</v-toolbar-title>
      
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          
        </v-row>
      </v-container>
    </v-content>
    <v-footer
      color="blue"
      app
    >
      <span class="white--text">&copy; 2020, Московский Авиационный Институт</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
    
  }
</script>