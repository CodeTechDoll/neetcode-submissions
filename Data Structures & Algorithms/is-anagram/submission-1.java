class Solution {
    public boolean isAnagram(String s, String t) {
        Hashtable<Character, Integer> table = new Hashtable();
        if (s.length() != t.length()) {
            return false;
        }


        for (char ch : s.toCharArray()) {
            if(table.containsKey(ch)) {
                table.replace(ch, table.get(ch) + 1);
            } else {
                table.put(ch, 1);
            }
        }
        for (char ch : t.toCharArray()) {
            if(!table.containsKey(ch)) {
                return false;
            } else {
                if(table.get(ch) == 1) {
                    table.remove(ch);
                } else {
                    table.replace(ch, table.get(ch) - 1);
                }
            }
        }

        return true;
    }
}
