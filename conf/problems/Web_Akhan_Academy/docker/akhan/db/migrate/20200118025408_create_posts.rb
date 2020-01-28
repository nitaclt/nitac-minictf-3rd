class CreatePosts < ActiveRecord::Migration[6.0]
  def change
    create_table :posts do |t|
      t.string :content
      t.boolean :is_public
      t.string :owner
      t.timestamps
    end
  end
end
