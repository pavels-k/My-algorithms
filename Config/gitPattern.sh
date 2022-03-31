# git
mkdir C:/develop/ #cоздаем папку на диске C (если Windows)
git clone https://github.com/pavels-k/vsc.git # копируем свой репозиторий на компьютер
cd title-repository/ #заходим в локальный репозиторий

git add . #производится индексирование файлов на предмет изменения в них
git commit -m "update" #фиксируем публикацию, комментируем изменения
git push -f #отправляем на сервер GitHub

git remote add origin https://github.com/pavels-k/vsc.git
git push -u origin master

echo "# kek" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/pavels-k/1lr.git
git push -u origin master

git config --global user.name 'имя_пользователя_github'
git config --global user.email 'ваша_электронная_почта'

git remote set-url origin https://github.com/pavels-k/1lr.git #изменить ссылку репозитория(в случае добавления нового проекта)
