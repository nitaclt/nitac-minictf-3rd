require 'sinatra'
require 'sinatra/activerecord'
require './models'
require 'securerandom'

disable :show_exceptions # hotfix (@st98_ pointed this out)
set :database, "sqlite3:akhan.db"
enable :sessions

ADMIN_SESSION_ID = "2ae96cac1e1659ef2231411ba36c8f77"

get '/' do
  session[:id] ||= SecureRandom.hex 16
  if session[:id] == ADMIN_SESSION_ID
    @posts = Post.all
  else
    @posts = Post.where(owner: session[:id]).or(Post.where(owner: ADMIN_SESSION_ID))
  end
  @id = session[:id]
  erb :index
end

post '/pic' do
  unless params[:file]
    halt "You need to select an image"
  end

  fn = params[:file][:filename]
  file = params[:file][:tempfile]

  unless [".png", ".jpg", ".svg"].include? File.extname(fn)
    halt "Only PNG, JPG, SVG images are allowed"
  end

  session[:pic] = fn
  
  open("public/images/#{fn}", 'wb') { |f| f.write file.read }

  redirect '/'
end

post '/post' do
  Post.create(
    content: params[:content],
    is_public: !!params[:is_public],
    owner: session[:id]
  )

  redirect '/'
end

# gives admin permission
get '/hey-crawler-845104ea3931ff88ab3d5dbb34249ff983b01410c67ac4cd8978ed1802177bbf' do
  session[:id] = ADMIN_SESSION_ID
end
